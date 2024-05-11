# HypGNOSIS

HypGNOSIS is a remote-controllable VR hypnosis app built on the LÖVR development framework.

## Requirements

- Docker
- docker-compose
- LÖVR

## Installation

### Webapp (Frontend and API)

1. `git clone https://github.com/mkflaher2/hypgnosis.git && cd hypgnosis`
2. Edit `hypgnosis.env` and set the hostname / IP address to the host you run HypGNOSIS on.
3. `docker-compose -f docker-compose.yaml up --build -d`

The webapp can be reached at `http://localhost:8080` on the host machine, or via your host IP from another.

### VR App

See https://lovr.org/docs/Getting_Started or https://lovr.org/docs/Getting_Started_(Quest) on how to load apps to your device.

#### Oculus Quest 2
1. Ensure that USB debugging is enabled on your Quest, and that it's connected to your computer.
2. From the `hypgnosis` directory: `adb push --sync lovr/. /sdcard/Android/data/org.lovr.app/files`
3. Using your headset, navigate to Library -> Applications -> Unknown sources, and launch LÖVR.
