#!/bin/bash

LOGFILE="logs/provisioning.log"
mkdir -p logs

echo "----------------------------" >> $LOGFILE
echo "$(date '+%Y-%m-%d %H:%M:%S') - Bash script started." >> $LOGFILE

# Simulating check for Nginx
echo "$(date '+%Y-%m-%d %H:%M:%S') - Checking if Nginx is installed..." >> $LOGFILE
sleep 0.1

# Simulating installation
echo "$(date '+%Y-%m-%d %H:%M:%S') - Nginx not found. Installing..." >> $LOGFILE
sleep 0.2

# Simulated success
echo "$(date '+%Y-%m-%d %H:%M:%S') - Nginx installed successfully (simulated)." >> $LOGFILE

echo "$(date '+%Y-%m-%d %H:%M:%S') - Bash script finished." >> $LOGFILE
echo "----------------------------" >> $LOGFILE
exit 0
