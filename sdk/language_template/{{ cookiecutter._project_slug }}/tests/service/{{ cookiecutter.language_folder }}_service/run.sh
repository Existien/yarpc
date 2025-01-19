#!/bin/bash
set -e -u

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
pushd $thisdir

# FIXME
# Replace 'exit -1' with commands to {% if not cookiecutter.use_separate_build_script %}compile and {% endif %}run this service
exit -1