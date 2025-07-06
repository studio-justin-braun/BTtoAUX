#!/bin/bash
# Install dependencies for BTtoAUX
set -e
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-tk git bluez pulseaudio

# Install Python packages if any
pip3 install --upgrade pip
pip3 install --upgrade pybluez

cat <<MSG
Installation complete. Use 'python3 src/main.py' to start the GUI.
MSG
