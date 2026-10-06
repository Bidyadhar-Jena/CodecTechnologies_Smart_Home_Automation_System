from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = Path(os.getenv("SMART_HOME_DB", DATA_DIR / "smart_home.db"))
HOST = os.getenv("SMART_HOME_HOST", "127.0.0.1")
PORT = int(os.getenv("SMART_HOME_PORT", "5000"))
DEBUG = os.getenv("SMART_HOME_DEBUG", "false").lower() == "true"
DEMO_MODE = os.getenv("SMART_HOME_DEMO", "true").lower() == "true"
REQUEST_TIMEOUT = float(os.getenv("TASMOTA_TIMEOUT", "4"))
