---
hide:
  - navigation
---

![ROTSE logo](assets/rotse.png){ .rotse-hero }

# ROTSE-IIIc Observer Manual

How to observe with **ROTSE-IIIc**, the robotic telescope at the H.E.S.S. site in Namibia.
The telescope is controlled with [pyobs](https://www.pyobs.org).

!!! danger "Emergency: roof won't close, or anything unsafe"
    :material-phone-alert: Call **TODO: name, phone number** immediately.
    All contacts: [Contacts](contacts.md).

!!! warning "Safety first"
    If you are unsure whether it is safe to open the roof, **don't**. Read
    [Weather & safety](weather-and-safety.md) before your first night.

## A night at a glance

<div class="grid cards" markdown>

-   :material-clipboard-check-outline: __1. Before you observe__

    ---

    Accounts, access, pre-night checklist.

    [:octicons-arrow-right-24: Before you observe](before-you-observe.md)

-   :material-power: __2. Startup__

    ---

    Bring the system up, check the weather, open the roof.

    [:octicons-arrow-right-24: Startup](startup.md)

-   :material-telescope: __3. Observing__

    ---

    Point, track and take images with the pyobs GUI.

    [:octicons-arrow-right-24: Observing](observing.md)

-   :material-power-sleep: __4. Shutdown__

    ---

    Park, close, check the roof is really closed.

    [:octicons-arrow-right-24: Shutdown](shutdown.md)

</div>

Something wrong? See [Troubleshooting](troubleshooting.md) or [Contacts](contacts.md).

## The system

| Part | What it is |
|---|---|
| Mount | Schier mount |
| Roof | Clamshell roof |
| Weather | Boltwood cloud sensor (TODO: list other weather inputs) |
| Software | pyobs modules on `ocs-server`, controlled from the pyobs GUI |
| Camera | TODO: camera, field of view, pixel scale, filters |

!!! note "This manual is a work in progress"
    Boxes marked **TODO** still need to be written. Found a mistake or something out of
    date? Tell **TODO: maintainer email**. See [About this manual](about.md).
