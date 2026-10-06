from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    ROOT / "README.md",
    ROOT / "app" / "app.py",
    ROOT / "app" / "config.py",
    ROOT / "app" / "database.py",
    ROOT / "app" / "requirements.txt",
    ROOT / "app" / "services" / "tasmota.py",
    ROOT / "app" / "services" / "automation.py",
    ROOT / "app" / "templates" / "base.html",
    ROOT / "app" / "templates" / "index.html",
    ROOT / "app" / "templates" / "devices.html",
    ROOT / "app" / "templates" / "automations.html",
    ROOT / "app" / "static" / "style.css",
    ROOT / "app" / "static" / "app.js",
    ROOT / "config" / "devices.example.json",
    ROOT / "docs" / "PROJECT_STRUCTURE.md",
    ROOT / "docs" / "SETUP.md",
    ROOT / "scripts" / "verify_project.py",
]

missing = [
    str(path.relative_to(ROOT))
    for path in required
    if not path.exists()
]

if missing:
    print("Missing required files:")
    print("\n".join(missing))
    sys.exit(1)

print("Project structure check: PASS")
print("Smart Home application structure found.")
print("Tasmota API integration found.")
