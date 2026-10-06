# Project Structure

```text
Smart-Home-Automation-System/
│
├── app/
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── requirements.txt
│   ├── services/
│   │   ├── tasmota.py        # Only Tasmota-specific application code
│   │   └── automation.py
│   ├── templates/
│   ├── static/
│   └── data/
├── config/
├── docs/
├── scripts/
├── README.md
├── LICENSE-APP.txt
├── THIRD_PARTY_NOTICES.md
└── .gitignore
```

## Tasmota integration
The project does not contain the Tasmota firmware source tree. The file `app/services/tasmota.py` contains the application's integration logic and sends commands to a separately installed Tasmota device through its local HTTP API.

## Architecture

```text
Browser → Flask → tasmota.py → Tasmota HTTP API → ESP8266/ESP32 → Device
                    │
                    └──────────→ SQLite
```
