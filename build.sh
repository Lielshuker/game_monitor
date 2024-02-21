#!/bin/bash
echo "docker compose is building"

docker compose  build --no-cache

echo "build finished"

echo "starting containers"

docker compose up -d



#https://stackoverflow.com/questions/57514720/bash-script-command-to-wait-until-docker-compose-process-has-finished-before-mov
