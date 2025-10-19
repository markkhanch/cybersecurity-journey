#!/bin/bash
# install.sh – Set up Python environment and enable interfaces on the Pi
#
# This script installs system packages, Python dependencies and enables
# SPI to prepare the Mini Hacker Pi environment.

set -euo pipefail

echo "Updating package lists..."
sudo apt-get update -y

echo "Installing system packages..."
sudo apt-get install -y python3 python3-pip python3-venv build-essential raspi-config

echo "Enabling SPI interface..."
sudo raspi-config nonint do_spi 0

echo "Adding current user to spi and gpio groups..."
sudo usermod -aG spi,gpio "$USER"

echo "Installing Python dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r "$(dirname "$0")/../src/shell/requirements.txt"

echo "Installation complete. You may need to reboot for group changes to take effect."