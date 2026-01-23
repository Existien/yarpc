#!/bin/bash
set -e -u

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
pushd $thisdir

uv sync --project ../yarpc
uv run --project ../yarpc yarpc definitions $@
