#!/bin/bash

set +x

if [ ! -e docker-compose ]; then
  curl -L --fail https://github.com/docker/compose/releases/download/1.22.0/run.sh -o docker-compose
  chmod +x docker-compose
fi

NAME="${PWD##*/}"
docker build --tag "${NAME}-selenium:latest" selenium
docker build --tag "${NAME}-runner:latest" runner
sed -e 's/@@NAME@@/'"$NAME"'/g' < docker-compose.yaml.in > docker-compose.yaml
