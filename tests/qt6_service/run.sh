#!/bin/bash
set -e -u

CMAKE=/Qt/6.5.3/gcc_64/bin/qt-cmake

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"
pushd $thisdir

$CMAKE -B/tmp/build_qt6 -S. -GNinja
cmake --build /tmp/build_qt6
/tmp/build_qt6/service