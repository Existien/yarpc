#!/bin/bash
set -e -u

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
pushd $thisdir
rm -rf html
sphinx-build -b html source html