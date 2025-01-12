#!/bin/bash
set -e -u

kill `cat /tmp/.xvfb_xfwm4_99.pid`
rm /tmp/.xvfb_xfwm4_99.pid