#!/bin/bash
LOGFILE="logs/provisioning.log"
mkdir -p logs
echo "Bash script started." >> $LOGFILE

if ! command -v nginx &> /dev/null; then
  echo "Installing Nginx." >> $LOGFILE
  sudo apt-get update && sudo apt-get install -y nginx || { 
    echo "Failed to install Nginx." >> $LOGFILE
    exit 1
  }
  echo "Nginx installed." >> $LOGFILE
else
  echo "Nginx already installed." >> $LOGFILE
fi

echo "Bash script finished." >> $LOGFILE
exit 0
# The script above installs Nginx and logs the output to a file called provisioning.log. If the installation fails, the script will log an error message and exit with a status code of 1. This allows the calling script to detect the failure and handle it appropriately.