#!/bin/bash
set -e -u

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
pushd $thisdir

uv --project ./test_library sync
uv --project ./test_library run robot Python.robot