# Homematic check_mk addon

This project contains an addon for the Homematic CCU2 or a Raspberrymatic/OpenCCU device which acts as an check_mk_agent.

As the orginal check_mk_agent does not support Busybox, not all of the sections of the original agent are available, but I tried to support as much as possible.

Additionally all datapoints of Homematic channels added to the Gewerk Monitored and all service messages are sent to the server in one section.

This is a fork of [fuf42/homematic_check_mk](https://github.com/fuf42/homematic_check_mk), which in turn is a fork of [alexreinert/homematic_check_mk](https://github.com/alexreinert/homematic_check_mk).

At the moment there are some Plugins for the check_mk server implemented:

- Check for Devices with Low Batteries (All devices)
- Check for Unreachable devices (All devices)
- Check for all other service messages (All devices)
- Check for Dutycycle (CCU and all connected LAN GW)
- Check for Humidity with configurable limits (Only channels in Gewerk Monitored)
- Check for installed addons and their updates
- Check for the CCU firmware and available updates

Don't hesitate to ask for additional check plugins.

# Changes in this fork

Addon 1.6 / MKP 1.4.4:

- Version lookup follows redirects (`curl -L`) and has a timeout. The old raspberrymatic.de address now redirects to openccu.de, which used to produce an empty "available" firmware version and a WARN.
- Empty or `n/a` update information (firmware, addons) is treated as "unknown" (OK with a note) instead of WARN. A real version difference still gives WARN.
- Removed a debug print that showed a raw dictionary in the service discovery output.
- New: SD card health plugin (see below).

# SD card health

The addon ships a plugin (`sdcard_health`) that reports as a local check:

- `SD card info`: identity of the card behind `/` or `/usr/local`
- `SD writes <card-id>`: GB written to the card since the plugin first saw it, with a daily rate. Default levels: WARN at 2000 GB, CRIT at 3500 GB. Adjust `WARN_GB` / `CRIT_GB` at the top of the script to the endurance of your card.
- `SD ext4 errors`: ext4 error counters and read-only remount of `/usr/local`
- `Pi power`: under-voltage and throttling (needs `vcgencmd`)

The write baseline is stored in `/usr/local/addons/sdcard_health/`, so it survives addon updates. On systems without an SD card, the plugin reports a single "no MMC/SD device found" info line.

# Installation
- CCU Addon: Use the normal addon installation process of the CCU/Raspberrymatic/OpenCCU
- check_mk Plugin: Refer to the check_mk documentation, how to install MKP packages. Requires Checkmk 2.3 or newer.

# License
Apache 2
