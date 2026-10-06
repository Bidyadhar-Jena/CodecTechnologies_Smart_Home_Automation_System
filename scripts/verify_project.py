from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT/"README.md",
    ROOT/"app"/"app.py",
    ROOT/"app"/"database.py",
    ROOT/"app"/"services"/"tasmota.py",
    ROOT/"app"/"templates"/"index.html",
    ROOT/"app"/"static"/"app.js",
    ROOT/"firmware"/"Tasmota-development"/"platformio.ini",
]
missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing:
    print("Missing required files:")
    print("\n".join(missing))
    sys.exit(1)
print("Project structure check: PASS")
print("Firmware source found.")
print("Custom Flask application found.")
