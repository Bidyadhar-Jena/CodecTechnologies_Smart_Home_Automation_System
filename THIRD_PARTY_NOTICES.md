# Third-Party Notices

## Tasmota
This project integrates with **Tasmota**, an open-source firmware project for ESP8266/ESP32 devices. The Tasmota firmware source is **not included** in this repository.

The application only communicates with a separately installed Tasmota device through its local HTTP API. The project's Tasmota-specific integration code is located at `app/services/tasmota.py`.

If you distribute Tasmota firmware itself, follow the licensing and attribution requirements of the Tasmota project.

## Python dependencies
The dashboard uses Flask and Requests. See `app/requirements.txt`.
