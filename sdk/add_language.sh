#!/bin/bash
set -e -u

if [ ! -f /.dockerenv ]; then
  echo "Script must be run from SDK."
  exit 1
fi

pushd /tmp
cookiecutter /workspace/sdk/language_template
