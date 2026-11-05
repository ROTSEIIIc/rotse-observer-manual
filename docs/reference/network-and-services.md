---
title: Network and services
description: Every computer and service at ROTSE-IIIc, with its address, port and how to check it.
tags:
  - maintenance
  - network
---

# Network and services

Every computer on the ROTSE-IIIc network, what runs on it, and how to check that it is alive.
Use this page when something shows no data (for example, the weather page is empty) and
you need to find out which machine or service stopped.

!!! info "No passwords on this page"
    Logins and passwords are not written here. TODO: say where they are kept (password
    manager, sealed sheet in the control room, ...).

!!! todo "TODO"
    Fill in the IP addresses once the site LAN is set up and each machine has a fixed
    address (DHCP reservation on the router). Also fill in the router and how to reach the
    site network from outside (VPN or jump host), or write where that is documented.

## Machines

| Machine | Hostname | IP address | Where it is | What runs on it |
|---|---|---|---|---|
| OCS server | `ocs-server` | TODO | TODO | XMPP server, all central pyobs modules, pyobs-weather and its databases, file cache, web-admin hub, Boltwood service. See [OCS server](#ocs-server). |
| Camera Pi (OTA) | TODO: `rotse-cam` or `ota-pi` | TODO | In the dome, on the telescope | QHY camera module, focuser module, web-admin spoke. See [Camera Pi](#camera-pi). |
| Weather mast Pi | TODO: `weather-mast`? | TODO | On the weather mast | Mast weather sensors (SHT45, BME280), allsky camera (indi-allsky). See [Weather mast Pi](#weather-mast-pi). |
| Archive server | TODO | — | Off-site | pyobs-archive: where observers download their data. |
| Router / switch | TODO | TODO | TODO | TODO |

!!! todo "TODO: camera Pi name"
    The setup guide calls the camera Pi `rotse-cam`, but its web-admin settings use
    `ota-pi`. Decide on one name and use it here.

## Quick check from any computer on the site network

Run these from a terminal on a computer on the site network. Replace a hostname with the
IP address from the table if the name does not resolve.

```bash
ping -c 3 ocs-server                                   # is the machine on?
curl -s http://ocs-server:8002/ | head -5              # pyobs-weather web page
curl -s http://<weather-mast-pi>:8082/api/v1/health    # mast sensors service
curl -s http://ocs-server:8081/api/v1/pyobs-weather    # Boltwood service
```

- `ping` gets no answer: the machine is off, has crashed, or is not on the network. Check
  power and the network cable first.
- `ping` works but `curl` fails: the machine is on, but the service is stopped. Log in to
  the machine and check the service (see the machine's section below).

## OCS server

The central computer. If it is down, nothing works: no GUI, no weather, no images.

| Service | Port | Address to open / check | What it does |
|---|---|---|---|
| ejabberd (XMPP) | 5222 | — (pyobs-gui connects to it) | Message server. All pyobs modules and the GUI talk through it. |
| pyobs modules | — | Seen as modules in pyobs-gui | Roof, mount, robotic, weather, acquisition, guiding, ImageWriter, ... |
| HttpFileCache | 37075 | `http://ocs-server:37075/` | Short-term store for new images. The camera uploads here; the ImageWriter and GUI download from here. |
| pyobs-web-admin (hub) | 8765 | `http://ocs-server:8765/` | Start, stop and restart pyobs modules on all machines from a browser. |
| pyobs-weather | 8002 | `http://ocs-server:8002/` | Weather website and the "is it safe to open?" decision for the robotic system. |
| pyobs-weather admin | 8002 | `http://ocs-server:8002/admin` | Stations, sensors and weather limits. Changes here change when the roof may open. |
| pyobs-weather worker (Celery) | — | — | Fetches all weather stations every few minutes. If it stops, weather values go stale. |
| PostgreSQL | 5432 | — (local only) | pyobs-weather's database: stations, sensors, limits. |
| RabbitMQ | 5672 | — (local only) | Message queue between the pyobs-weather website and its worker. |
| InfluxDB | 8086 | `http://ocs-server:8086/` | Weather history (time series) used for plots. |
| Boltwood service | 8081 | `http://ocs-server:8081/api/v1/pyobs-weather` | Reads the Boltwood cloud sensor over RS-485 and serves it as JSON to pyobs-weather. |
| Astrometry | TODO | TODO | Plate solving for acquisition (pointing corrections). |

!!! danger "pyobs-weather admin"
    The weather limits in the admin decide when the roof is allowed to open. Do not change
    them unless the telescope team asked you to.

!!! todo "TODO: OCS server"
    - Confirm every port above on the real server. The ports for PostgreSQL, RabbitMQ and
      InfluxDB are the defaults from the test setup, not checked on `ocs-server`.
    - How pyobs-weather and its databases run (Docker or system services) and the command to
      restart them.
    - Astrometry: the current acquisition config sends images to
      `https://astrometry.monet.uni-goettingen.de/` (off-site). If a local astrometry service
      is installed on `ocs-server`, add its port and how to check it.
    - Where the nightly images are stored on disk (ImageWriter spool) and how full the disk is
      allowed to get.
    - How to log in (SSH user, where the key/password is).

## Camera Pi

Runs the camera and the focuser. Talks to `ocs-server` over XMPP (port 5222) and uploads
images to the file cache on `ocs-server` (port 37075).

| Service | Port | Address to open / check | What it does |
|---|---|---|---|
| pyobs camera module | — | Seen as a module in pyobs-gui | QHY camera |
| pyobs focuser module | — | Seen as a module in pyobs-gui | Focuser |
| pyobs-web-admin (spoke) | 8765 | `http://<camera-pi>:8765/` | Start/stop the camera and focuser modules. Normally used through the hub on `ocs-server`. |

If the camera is missing in pyobs-gui but the Pi answers `ping`, restart the camera module in
web-admin (see [Restarting machines and services](../maintenance/restart-services.md)).

!!! todo "TODO: Camera Pi"
    Hostname (see above), IP, how to log in, and who to call if it does not come back.

## Weather mast Pi

A Raspberry Pi 5 on the weather mast. Reads the mast temperature, humidity and pressure
sensors and runs the allsky camera.

| Service | Port | Address to open / check | What it does |
|---|---|---|---|
| Mast sensors (`rotse-weather-mast`) | 8082 | `http://<weather-mast-pi>:8082/api/v1/sensors` | Latest SHT45 and BME280 readings. pyobs-weather reads them from here. |
| Mast sensors: health | 8082 | `http://<weather-mast-pi>:8082/api/v1/health` | Is the service running, and is each sensor working? |
| indi-allsky | TODO | TODO | Allsky camera images. |

### Weather mast Pi is down or shows no data

1. Open `http://<weather-mast-pi>:8082/api/v1/sensors` in a browser.
    - *No page at all:* go to step 2.
    - *Page loads, but a sensor has `"ok": false`:* the service runs but that sensor has a
      problem. The `error` field says what. A large `age_s` means the reading is old.
2. Run `ping <weather-mast-pi>`.
    - *No answer:* the Pi is off or not on the network. Check its power and network cable.
    - *Answers:* the Pi is on but the service has stopped. Go to step 3.
3. Log in to the Pi and run:
   ```bash
   systemctl status rotse-weather-mast
   journalctl -u rotse-weather-mast -n 50
   ```
4. Restart it with `sudo systemctl restart rotse-weather-mast`. *You should see:* the
   `sensors` page loads again and both sensors show `"ok": true`.

!!! todo "TODO: Weather mast Pi"
    Hostname, IP, how to log in, the indi-allsky port and service name, and who to call if a
    sensor stays broken.

## Off-site

| Service | Address | What it does |
|---|---|---|
| pyobs-archive | TODO | Where observers find their images. |

## If something goes wrong

- A machine or service is down: [Restarting machines and services](../maintenance/restart-services.md).
- Symptoms an observer sees: [Troubleshooting](../troubleshooting.md).
