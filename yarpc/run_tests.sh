#!/bin/bash
set -e -u

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
pushd $thisdir

uv sync --group dev
uv run pytest tests