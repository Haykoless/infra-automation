#!/bin/bash
# A simple script to install and configure Nginx

# Check if Nginx is installed
if ! command -v nginx &> /dev/null; then
    echo "Nginx not found. Installing..."
    if sudo apt-get update && sudo apt-get install -y nginx; then
        echo "Nginx installed successfully."
    else
        echo "Error: Failed to install Nginx." >&2
        exit 1
    fi
else
    echo "Nginx is already installed."
fi

exit 0