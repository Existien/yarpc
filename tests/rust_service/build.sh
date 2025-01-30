#!/bin/bash
set -e -u

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
pushd $thisdir

# FIXME
# Replace 'exit -1' with commands to compile this service
exit -1