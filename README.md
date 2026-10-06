# Smart Home Automation System

A practical smart-home control platform built with **Python, Flask, SQLite, JavaScript, and the Tasmota HTTP API**. The application provides a web dashboard for controlling and monitoring Tasmota-compatible ESP8266/ESP32 smart devices.

## What this project provides
- Room-based smart-device dashboard
- Device registration and status tracking
- Switch control through the Tasmota HTTP API
- Demo/simulation mode without physical hardware
- SQLite persistence for devices and automation rules
- State-based automation rules
- REST endpoints for dashboard integration
- Clean separation between your application code and the external Tasmota firmware

## Project Structure
```text
Smart-Home-Automation-System/
│
├── app/
│   ├── app.py                    # Flask application and REST routes
│   ├── config.py                 # Application configuration
│   ├── database.py               # SQLite database and CRUD operations
│   ├── requirements.txt          # Python dependencies
│   │
│   ├── services/
│   │   ├── tasmota.py            # Tasmota HTTP API integration
│   │   └── automation.py         # Automation rule engine
│   │
│   ├── templates/
│   │   ├── base.html             # Shared page layout
│   │   ├── index.html             # Main dashboard
│   │   ├── devices.html           # Device management
│   │   └── automations.html       # Automation management
│   │
│   ├── static/
│   │   ├── style.css              # Dashboard styling
│   │   └── app.js                 # Frontend JavaScript
│   │
│   └── data/
│       └── smart_home.db          # Created automatically when the app runs
│
├── config/
│   └── devices.example.json       # Example device configuration
│
├── docs/
│   ├── PROJECT_STRUCTURE.md        # Detailed project structure
│   └── SETUP.md                    # Installation and hardware setup
│
├── scripts/
│   └── verify_project.py           # Project validation script
│
├── README.md
├── LICENSE-APP.txt                # License for the custom application
├── THIRD_PARTY_NOTICES.md         # External software/API notice
└── .gitignore
```

> **Important:** This repository does **not** include the Tasmota firmware source code. `app/services/tasmota.py` is the only Tasmota-specific file in this project. It communicates with a Tasmota-compatible device through its local HTTP API.

## Architecture
```text
Browser
   │
   ▼
Flask Dashboard
   │
   ├── SQLite
   │
   └── app/services/tasmota.py
            │
            ▼
     Tasmota HTTP API
            │
            ▼
      ESP8266 / ESP32
            │
            ▼
     Relay / Light / Fan / Plug
```

## Quick Start
```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r app/requirements.txt
```

Start the application:
```bash
python app/app.py
```

Open `http://127.0.0.1:5000` in your browser.

The dashboard starts in **demo mode**, so it can be demonstrated without physical hardware.

## Real Tasmota Devices
1. Flash a supported ESP8266/ESP32 board with Tasmota.
2. Connect the device to your local Wi-Fi network.
3. Give it a stable local IP address.
4. Add the device IP from the dashboard.
5. Use the dashboard to control the device.

The application communicates with Tasmota using its local HTTP command API.

## Technologies
- Python
- Flask
- SQLite
- HTML5 / CSS3 / JavaScript
- Tasmota HTTP API
- ESP8266 / ESP32

## Project Status
**Portfolio/academic project - ready for local demonstration and further hardware integration.**

## Licensing
The custom application is provided under `LICENSE-APP.txt`. Tasmota is an external firmware project and is **not bundled in this repository**. See `THIRD_PARTY_NOTICES.md` for details.
