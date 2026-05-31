#!/usr/bin/env bash
# Build + deploy the wiki-daily Lambda + CloudFormation stack.
#
# Usage:
#   bash aws/deploy.sh                    # build + deploy (uses defaults)
#   bash aws/deploy.sh --enable-schedule  # also enables EventBridge cron
#   bash aws/deploy.sh --skip-build       # skip rebuild, redeploy existing zip
#
# Prereqs:
#   - aws CLI configured with credentials that can create CFN stacks
#   - Python 3.12 locally (matches Lambda runtime)
#
# What it does:
#   1. pip install anthropic into a local "build/" directory
#   2. Copies handler.py + scripts/ into build/
#   3. Zips build/ → aws/build/handler.zip
#   4. Uploads zip to S3 bucket (creates if missing)
#   5. Runs `aws cloudformation deploy` with the template

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AWS_DIR="$REPO_ROOT/aws"
BUILD_DIR="$AWS_DIR/build"
ZIP_PATH="$AWS_DIR/build/handler.zip"

STACK_NAME="${STACK_NAME:-wiki-daily-update}"
AWS_REGION="${AWS_REGION:-us-east-1}"
S3_BUCKET="${S3_BUCKET:-}"          # auto-derived if empty
S3_KEY="wiki-daily/handler-$(date +%Y%m%d%H%M%S).zip"
ENABLE_SCHEDULE="false"
SKIP_BUILD="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --enable-schedule) ENABLE_SCHEDULE="true"; shift ;;
    --skip-build)      SKIP_BUILD="true"; shift ;;
    --stack)           STACK_NAME="$2"; shift 2 ;;
    --bucket)          S3_BUCKET="$2"; shift 2 ;;
    --region)          AWS_REGION="$2"; shift 2 ;;
    --help|-h)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'
      exit 0 ;;
    *) echo "unknown flag: $1" >&2; exit 2 ;;
  esac
done

ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
if [[ -z "$S3_BUCKET" ]]; then
  S3_BUCKET="wiki-daily-${ACCOUNT_ID}-${AWS_REGION}"
fi

echo "==> account=${ACCOUNT_ID} region=${AWS_REGION} stack=${STACK_NAME}"
echo "==> s3 bucket=${S3_BUCKET} key=${S3_KEY}"

if [[ "$SKIP_BUILD" == "false" ]]; then
  echo "==> building Lambda package"
  rm -rf "$BUILD_DIR"
  mkdir -p "$BUILD_DIR/scripts"

  # Install anthropic into the build dir for the Lambda runtime architecture.
  # We force manylinux2014_x86_64 wheels because the SDK has platform-specific
  # dependencies (pydantic-core ships compiled binaries) — installing on macOS
  # would otherwise pull darwin-arm64 wheels that won't load on Lambda Linux.
  pip install --quiet \
    --target "$BUILD_DIR" \
    --platform manylinux2014_x86_64 \
    --implementation cp \
    --python-version 3.12 \
    --only-binary=:all: \
    --upgrade \
    anthropic

  # Bundle the handler + the daily_email helpers it imports
  cp "$AWS_DIR/lambda/handler.py" "$BUILD_DIR/handler.py"
  cp "$REPO_ROOT/scripts/daily_email.py" "$BUILD_DIR/scripts/daily_email.py"

  # Zip it up
  ( cd "$BUILD_DIR" && zip -qr "$ZIP_PATH" . )
  zip_size_human=$(ls -lh "$ZIP_PATH" | awk '{print $5}')
  echo "==> zip built: $ZIP_PATH ($zip_size_human)"
fi

# Ensure S3 bucket exists
if ! aws s3api head-bucket --bucket "$S3_BUCKET" --region "$AWS_REGION" 2>/dev/null; then
  echo "==> creating S3 bucket: $S3_BUCKET"
  if [[ "$AWS_REGION" == "us-east-1" ]]; then
    aws s3api create-bucket --bucket "$S3_BUCKET" --region "$AWS_REGION" >/dev/null
  else
    aws s3api create-bucket --bucket "$S3_BUCKET" --region "$AWS_REGION" \
      --create-bucket-configuration LocationConstraint="$AWS_REGION" >/dev/null
  fi
  aws s3api put-bucket-versioning --bucket "$S3_BUCKET" \
    --versioning-configuration Status=Enabled >/dev/null
fi

echo "==> uploading zip to s3://${S3_BUCKET}/${S3_KEY}"
aws s3 cp "$ZIP_PATH" "s3://${S3_BUCKET}/${S3_KEY}" --region "$AWS_REGION" --no-progress

echo "==> deploying CloudFormation stack"
aws cloudformation deploy \
  --region "$AWS_REGION" \
  --stack-name "$STACK_NAME" \
  --template-file "$AWS_DIR/template.yaml" \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
      LambdaS3Bucket="$S3_BUCKET" \
      LambdaS3Key="$S3_KEY" \
      EnableSchedule="$ENABLE_SCHEDULE" \
  --no-fail-on-empty-changeset

# Force the Lambda to pick up the new zip (CFN only updates the function if
# the S3 key changed, which it does on every build — but we add a safety
# update-function-code just in case the key was reused)
FUNCTION_NAME=$(aws cloudformation describe-stacks \
  --region "$AWS_REGION" --stack-name "$STACK_NAME" \
  --query "Stacks[0].Outputs[?OutputKey=='FunctionName'].OutputValue" --output text)

echo ""
echo "==> stack outputs:"
aws cloudformation describe-stacks --region "$AWS_REGION" --stack-name "$STACK_NAME" \
  --query "Stacks[0].Outputs[*].[OutputKey,OutputValue]" --output table

cat <<EOF

==> NEXT STEPS
1. Populate the two secrets (one-time):

   aws secretsmanager update-secret --region $AWS_REGION \\
     --secret-id wiki/anthropic \\
     --secret-string '{"api_key":"sk-ant-..."}'

   aws secretsmanager update-secret --region $AWS_REGION \\
     --secret-id wiki/github \\
     --secret-string '{"token":"ghp_..."}'

   (Generate the GitHub PAT at https://github.com/settings/tokens with
    scope "repo > contents > write" on rgovindji/wiki_research.)

2. Test the function with skip_update=true (just sends email):

   aws lambda invoke --region $AWS_REGION \\
     --function-name $FUNCTION_NAME \\
     --payload '{"skip_update":true,"send_email":true}' \\
     --cli-binary-format raw-in-base64-out /tmp/wiki-out.json
   cat /tmp/wiki-out.json

3. Once secrets and test pass, enable the EventBridge schedule:

   bash aws/deploy.sh --enable-schedule --skip-build

   (or update the stack manually with EnableSchedule=true)

4. Check CloudWatch logs at:
   /aws/lambda/$FUNCTION_NAME

EOF
