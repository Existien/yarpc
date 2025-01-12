#!/bin/bash
set -e -u

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
pushd $thisdir

# Regenerate code
./generate.sh

# Build software under test
pushd qt6_service
./build.sh
popd

# Install behave test requirements
if [ ! -d "behave-tests/.venv" ];then
    python3 -m venv behave-tests/.venv
fi
. behave-tests/.venv/bin/activate
pip install -r behave-tests/requirements.txt

# Start tests
behave behave-tests
