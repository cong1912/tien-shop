#!/bin/sh

set -e

cd $PLATFORM_ROOT

export $(cat .deploy_env | xargs)

# pull all
#git submodule foreach --recursive git checkout develop
#git submodule foreach --recursive git pull origin develop

# pull specific submodule
echo "CI_MERGE_REQUEST_TARGET_BRANCH_NAME=$CI_MERGE_REQUEST_TARGET_BRANCH_NAME"
echo "CI_COMMIT_BRANCH=$CI_COMMIT_BRANCH"
echo "CI_COMMIT_REF_NAME=$CI_COMMIT_REF_NAME"
echo "SERVICE_TO_DEPLOY=$SERVICE_TO_DEPLOY"

cd $SERVICE_TO_DEPLOY
DEPLOY_BRANCH=${CI_MERGE_REQUEST_TARGET_BRANCH_NAME:-develop}
git checkout $DEPLOY_BRANCH
git pull origin $DEPLOY_BRANCH

IS_DEPS_CHANGED=`git --no-pager diff --name-only HEAD~1 -- requirements.txt`

cd ..

DEPLOY_MODE=${DEPLOY_MODE:-dev}
DOCKERCOMPOSE_FILE="docker-compose.${DEPLOY_MODE,,}.yml"

# Check if requirements.txt changed
if [ ! -z "$IS_DEPS_CHANGED" ]; then
    echo "Deps change. Re-build docker image..."
    docker-compose -f $DOCKERCOMPOSE_FILE up -d --build $SERVICE_TO_DEPLOY
else
    echo "Deps not changed. Skip re-build docker image"
fi

# Compile i18n for Storefront
[[ "$SERVICE_TO_DEPLOY" == "storefront" ]] && docker-compose -f $DOCKERCOMPOSE_FILE exec -T $SERVICE_TO_DEPLOY django-admin compilemessages

docker-compose -f $DOCKERCOMPOSE_FILE restart $SERVICE_TO_DEPLOY

echo ""
echo "All Done."
echo ""
