#!/bin/bash
set -e -u

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
pushd $thisdir

if [ ! -d "behave-tests/.venv" ];then
    python3 -m venv behave-tests/.venv
fi
. behave-tests/.venv/bin/activate
pip install -r behave-tests/requirements.txt

behave behave-tests $@