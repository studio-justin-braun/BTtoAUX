# BTtoAUX

BTtoAUX provides a graphical interface to play audio from any Bluetooth device through the Raspberry Pi's audio output. It is designed for a 320x480 touch display and works on the Raspberry Pi 4.

## Features

- Bluetooth pairing with PIN confirmation
- Display of connected device, track title and artist
- Playback controls: previous, play/pause, next
- Progress indicator and remaining time
- Volume control
- Update script to fetch the latest version from GitHub

## Requirements

- Raspberry Pi 4 running Raspberry Pi OS
- 320x480 touch display
- Internet connection for updates

## Installation

Run the included `install.sh` script to install all dependencies:

```bash
bash install.sh
```

Start the GUI with:

```bash
python3 src/main.py
```

## Updating

Use `update.sh` to check for and download newer versions from GitHub:

```bash
bash update.sh
```

## Disclaimer

This project currently provides a basic GUI. Integration with Bluetooth audio and system services requires additional setup that is not included here.
