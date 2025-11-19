#!/bin/bash

cd /home/j/bin/mouse_clicker
source /home/j/bin/mouse_clicker/venv/bin/activate
export DISPLAY=:0
export XAUTHORITY=$(find /run/user/$(id -u)/ -name Xauthority | head -n 1)

sleep $((RANDOM % 300))

python /home/j/bin/mouse_clicker/clicker.py
deactivate
