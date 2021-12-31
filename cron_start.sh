#!/bin/bash
crontab -l | { cat; echo "*/1 * * * * python /home/pi/Desktop/startup_script/startup.py"; } | crontab -