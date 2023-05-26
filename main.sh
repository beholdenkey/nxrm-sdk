#!/bin/bash
# This script is used to generate the nexus_sdk library for python using the openapi-generator-cli

openapi-generator-cli generate \
    -i openapi.json \
    -g python \
    -o nexus_sdk \
    --package-name nexus_sdk \
    --git-user-id beholdenkey \
    --git-repo-id nexus-sdk \
    --additional-properties=packageName=nexus_sdk,packageVersion=0.0.1,projectName=nexus-sdk,projectVersion=0.0.1
