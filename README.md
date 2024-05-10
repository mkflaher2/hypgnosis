# HypGNOSIS

HypGNOSIS is a remote-controllable VR hypnosis app built on the LÖVR development framework.

## Requirements

- python3.10
- python3.10-venv
- LÖVR

## Installation

TODO: make webapp deployable via docker

### Webapp (Frontend and API)

1. `git clone https://github.com/mkflaher2/hypgnosis.git && cd hypgnosis`
2. `python -m venv . && source bin/activate`
3. `pip install -r requirements.txt`
4. For the API: `python api.py`
5. `export HYPGNOSIS_API_URL=http://localhost:8081`
5. For the frontend: `python ui.py`

The webapp can be reached at `http://localhost:8080`

### VR App

See https://lovr.org/docs/Getting_Started or https://lovr.org/docs/Getting_Started_(Quest) on how to load apps to your device.
