#!/bin/bash

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
pushd $thisdir
docker build -t yarpc-sdk .