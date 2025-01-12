#!/bin/bash
set -e -u

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
pushd $thisdir

pdm install -p ../yarpc
pdm run -p ../yarpc yarpc definitions $@
