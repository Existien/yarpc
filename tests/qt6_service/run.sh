#!/bin/bash
set -e -u

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
${thisdir}/build.sh
/tmp/build_qt6/service