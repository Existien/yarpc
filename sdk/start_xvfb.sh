#!/bin/bash
set -e -u

xvfb-run --server-num=99 --server-args="-ac -screen 0 1280x800x24" dbus-run-session xfwm4 &
PID=$!
sleep 4

XFWM4PID=`pstree -T -p $PID | grep xfwm4 | sed 's/^.*xfwm4.*(\([0-9]\+\))/\1/'`
echo $XFWM4PID > /tmp/.xvfb_xfwm4_99.pid