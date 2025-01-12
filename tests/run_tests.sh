#!/bin/bash
set -e -u

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
pushd $thisdir

# Regenerate code
./generate.sh

# Install behave test requirements
if [ ! -d "behave-tests/.venv" ];then
    python3 -m venv behave-tests/.venv
fi
. behave-tests/.venv/bin/activate
pip install -r behave-tests/requirements.txt

if [[ $# == 0 ]];then
    languages=(qt6 python)
else
    languages=$@
fi

# Run python tests
if [[ ${languages[*]} =~ "python" ]];then
    behave behave-tests/python
fi

# Run Qt6 tests
if [[ ${languages[*]} =~ "qt6" ]];then
    pushd qt6_service
    ./build.sh
    popd
    $thisdir/../sdk/start_xvfb.sh
    export DISPLAY=:99
    behave behave-tests/qt6
    $thisdir/../sdk/stop_xvfb.sh
fi
