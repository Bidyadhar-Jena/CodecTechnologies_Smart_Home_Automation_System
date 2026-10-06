# Setup and Demonstration Guide

## Software-only demonstration
1. Install Python 3.10+.
2. Create and activate a virtual environment.
3. Run:
```bash
pip install -r app/requirements.txt
python app/app.py
```
4. Open `http://127.0.0.1:5000`.
5. Toggle demo devices.
6. Add an automation rule.
7. Use **Run enabled rules now** to execute matching rules.

Demo mode is enabled by default.

## Real Tasmota device
1. Flash a supported ESP8266/ESP32 board with Tasmota separately; the firmware source is not included in this repository.
2. Connect it to your local Wi-Fi.
3. Give it a stable local IP.
4. Add the device IP from the dashboard.
5. Toggle its power from the dashboard.

The application uses Tasmota's local HTTP command endpoint through `app/services/tasmota.py`.

## Security
Do not expose the Tasmota web interface or this dashboard directly to the public internet without authentication, network controls and HTTPS.
