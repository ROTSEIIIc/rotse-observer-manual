![ROTSE logo](assets/rotse.png){ .rotse-hero }

# ROTSE-IIIc Observer Manual

How to observe with **ROTSE-IIIc**, the robotic telescope at the H.E.S.S. site in Namibia,
and how to keep it running. The telescope is controlled with [pyobs](https://www.pyobs.org).

!!! danger "Emergency: roof won't close, or anything unsafe"
    Call **TODO: name, phone number** immediately.
    All contacts: [Contacts](contacts.md).

!!! warning "Safety first"
    If you are unsure whether it is safe to open the roof, **don't**. Read
    [Weather and safety](weather-and-safety.md) before your first night.

The manual has three parts. Pick the one that fits what you are doing.

## Observer guide

For observers. Read in this order before your first night.

| Page | What it covers |
|---|---|
| [Before you observe](before-you-observe.md) | Accounts, software, access. Once. |
| [Weather and safety](weather-and-safety.md) | When the roof may open, and what closes it |
| [Startup](startup.md) | Bring the system up and open the roof |
| [Observing](observing.md) | Point, track and take images |
| [Shutdown](shutdown.md) | Park, close, check the roof is really closed |
| [Troubleshooting](troubleshooting.md) | What to do when something goes wrong |

## Maintenance

For someone at the telescope who must fix something or do it by hand.

| Page | What it covers |
|---|---|
| [Safety on site](maintenance/safety.md) | Read first, before working at the telescope |
| [Dry air pump](maintenance/dry-air-pump.md) | When and how to run the dry air pump on the camera |
| [Manual roof operation](maintenance/manual-roof.md) | Close or open the roof by hand |
| [Severe mount faults](maintenance/mount-severe-fault.md) | Mount stuck, faulted or in a limit |
| [Restarting machines and services](maintenance/restart-services.md) | A computer, service or pyobs module is down |

## Reference

How the system is built.

| Page | What it covers |
|---|---|
| [Network and services](reference/network-and-services.md) | Every machine, IP address, port and web address, and how to check them |

## The system

| Part | What it is |
|---|---|
| Mount | Schier mount |
| Roof | Clamshell roof |
| Camera | QHY camera with focuser. TODO: model, field of view, pixel scale, filters |
| Weather | Boltwood cloud sensor, weather mast (temperature, humidity, pressure), allsky camera |
| Software | pyobs modules on `ocs-server`, controlled from the pyobs GUI |

!!! note "This manual is a work in progress"
    Boxes marked **TODO** still need to be written. Found a mistake or something out of
    date? Tell **TODO: maintainer email**. See [About this manual](about.md).
