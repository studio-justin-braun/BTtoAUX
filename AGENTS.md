# AGENT Instructions

This repository contains the BTtoAUX project. It provides a simple GUI written in Python (`src/main.py`) that is intended to run on a Raspberry Pi 4 with a 320x480 touch screen. The GUI shows track information and basic playback controls. Bluetooth integration uses simple `bluetoothctl` commands to enable discoverability and detect a connected device, but functionality is still limited.

## Coding Guidelines

- Keep all source code in the `src/` directory.
- Use Python 3.7+ compatible syntax.
- Use PEP8 style where possible.
- When modifying or adding scripts, update this `AGENTS.md` file accordingly.
  The project root contains helper shell scripts such as `install.sh`,
  `update.sh` and `setup_bt_sink.sh`.
- Always run `flake8` and `python -m py_compile` on any added Python files when possible.

## Programmatic Checks

Run the following commands before committing:

```bash
flake8 src/main.py
python -m py_compile src/main.py
```

These checks ensure the code is syntactically correct and roughly follows style guidelines. If `flake8` is not installed, it can be installed with `pip install flake8`.

## Pull Request Notes

Include a summary of changes and test results in the PR description. Mention any limitations or manual steps required for setup.

