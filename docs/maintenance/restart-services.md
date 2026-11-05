# Restarting machines and services

How to bring a stopped computer, service or pyobs module back. To find out what is down,
first do the [quick check](../reference/network-and-services.md#quick-check-from-any-computer-on-the-site-network).

!!! warning "Is the roof open?"
    Restarting `ocs-server` or the roof module can stop roof control. Close the roof first
    if you can. TODO: what happens to the roof while `ocs-server` restarts.

## A pyobs module

Use web-admin on `ocs-server` (`http://ocs-server:8765/`). It starts and stops modules on all
machines.

1. Log in. TODO: where the login is.
2. Find the module. TODO: screenshot.
3. Click TODO: button name.
   *You should see:* the module appears again in the pyobs GUI.

## A service on a Linux machine

For services that are not pyobs modules (weather mast sensors, Boltwood, pyobs-weather, ...).
The service names are in [Network and services](../reference/network-and-services.md).

1. Log in to the machine with SSH. TODO: user, where the key is.
2. See whether it runs, and why it stopped:
   ```bash
   systemctl status <service>
   journalctl -u <service> -n 50
   ```
3. Restart it:
   ```bash
   sudo systemctl restart <service>
   ```
4. Check it again with `systemctl status <service>`. *You should see:* `active (running)`.

## A whole machine

!!! todo "TODO"
    - Safe order to switch machines off and on (for example `ocs-server` first, then the
      Pis?), and what must be closed or parked first.
    - Where each power switch is. Can it be power-cycled remotely (smart plug, PDU)?
    - What starts by itself after a reboot, and what must be started by hand.

## After a power cut

!!! todo "TODO"
    Step-by-step: what to check and in which order after the power comes back.
