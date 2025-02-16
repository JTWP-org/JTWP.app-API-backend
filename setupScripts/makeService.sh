#!/bin/bash

# Set your user and group
USER_NAME="steam"
GROUP_NAME="steam"

# Get the full path of the current directory
#if u dont run this in the path u must enter a valid path
PROJECT_DIR=$(pwd)

# Path to the systemd service file
SERVICE_FILE="/etc/systemd/system/main_api.service"

# Create the systemd service file using the full path
sudo tee $SERVICE_FILE > /dev/null <<EOF
[Unit]
Description=Flask API Service for Main API
After=network.target

[Service]
User=${USER_NAME}
Group=${GROUP_NAME}
WorkingDirectory=${PROJECT_DIR}
ExecStart=/usr/bin/python3 ${PROJECT_DIR}/main_api.py
Restart=always
RestartSec=5
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd to pick up the new service file
sudo systemctl daemon-reload

# Enable the service to start on boot and start it now
sudo systemctl enable main_api.service
sudo systemctl start main_api.service

echo "Service 'main_api' has been set up and started."