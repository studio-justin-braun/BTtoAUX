#!/bin/bash
# Install dependencies for BTtoAUX
set -e
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-tk git bluez pulseaudio

# Install Python packages if any
pip3 install --break-system-packages --upgrade pip
# PyBluez is not installed automatically due to incompatibility with
# newer Python versions. Install manually if needed.

cat <<MSG
Installation complete. Use 'python3 src/main.py' to start the GUI.
MSG

