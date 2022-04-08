#!/bin/sh

echo PLATFORM_ROOT=$PLATFORM_ROOT >> .env
echo SERVICE_TO_DEPLOY=$SERVICE_TO_DEPLOY >> .env

echo DEBUG=0 >> .env
echo SQL_ENGINE=django.db.backends.postgresql >> .env
echo DATABASE=postgres >> .env

echo SECRET_KEY=$SECRET_KEY >> .env
echo SQL_DATABASE=$SQL_DATABASE >> .env
echo SQL_USER=$SQL_USER >> .env
echo SQL_PASSWORD=$SQL_PASSWORD >> .env
echo SQL_HOST=$SQL_HOST >> .env
echo SQL_PORT=$SQL_PORT >> .env
echo WEB_IMAGE=$IMAGE:web  >> .env
echo NGINX_IMAGE=$IMAGE:nginx  >> .env
echo CI_REGISTRY_USER=$CI_REGISTRY_USER   >> .env
echo CI_JOB_TOKEN=$CI_JOB_TOKEN  >> .env
echo CI_REGISTRY=$CI_REGISTRY  >> .env
echo CI_MERGE_REQUEST_TARGET_BRANCH_NAME=$CI_MERGE_REQUEST_TARGET_BRANCH_NAME  >> .env
echo CI_COMMIT_BRANCH=$CI_COMMIT_BRANCH  >> .env
echo CI_COMMIT_REF_NAME=$CI_COMMIT_REF_NAME  >> .env
echo IMAGE=$CI_REGISTRY/$CI_PROJECT_NAMESPACE/$CI_PROJECT_NAME >> .env
