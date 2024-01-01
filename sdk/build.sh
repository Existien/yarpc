#!/bin/bash

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
docker build -t yarpc-sdk .