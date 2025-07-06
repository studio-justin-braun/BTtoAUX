#!/bin/bash
# Configure Raspberry Pi as Bluetooth A2DP sink and route audio to 3.5mm jack
# This script installs necessary packages, starts PulseAudio, and enables
# Bluetooth pairing for a smartphone. Run once after boot.

set -e

# Install required packages
sudo apt-get update
sudo apt-get install -y pulseaudio pulseaudio-module-bluetooth bluez-utils

# Ensure PulseAudio is running
if ! pgrep -x pulseaudio >/dev/null; then
    pulseaudio --start
fi

# Set audio output to analog 3.5mm jack
if command -v amixer >/dev/null; then
    sudo amixer cset numid=3 1 || true
fi

# Load Bluetooth modules for PulseAudio
pactl unload-module module-bluetooth-discover 2>/dev/null || true
pactl load-module module-bluetooth-discover
pactl unload-module module-bluetooth-policy 2>/dev/null || true
pactl load-module module-bluetooth-policy

# Enable discoverable & pairable mode
bluetoothctl <<BTPAIR
power on
agent on
default-agent
discoverable on
pairable on
BTPAIR

echo "Raspberry Pi ready for Bluetooth pairing. Connect from your smartphone and play audio."
