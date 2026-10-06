import sqlite3
from config import DATABASE_PATH, DATA_DIR

SCHEMA = """
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    room TEXT NOT NULL,
    ip_address TEXT,
    device_type TEXT NOT NULL DEFAULT 'Switch',
    power_state INTEGER NOT NULL DEFAULT 0,
    online INTEGER NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS automations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    device_id INTEGER NOT NULL,
    trigger_state INTEGER NOT NULL,
    action_state INTEGER NOT NULL,
    enabled INTEGER NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(device_id) REFERENCES devices(id) ON DELETE CASCADE
);
"""

SEED_DEVICES = [
    ("Living Room Light", "Living Room", "", "Light", 0, 1),
    ("Bedroom Fan", "Bedroom", "", "Fan", 0, 1),
    ("Study Light", "Study Room", "", "Light", 1, 1),
    ("Kitchen Plug", "Kitchen", "", "Plug", 0, 1),
]

def get_connection():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_connection()
    conn.executescript(SCHEMA)
    count = conn.execute("SELECT COUNT(*) AS count FROM devices").fetchone()["count"]
    if count == 0:
        conn.executemany(
            "INSERT INTO devices (name, room, ip_address, device_type, power_state, online) VALUES (?, ?, ?, ?, ?, ?)",
            SEED_DEVICES,
        )
    conn.commit()
    conn.close()

def list_devices():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM devices ORDER BY room, name").fetchall()
    conn.close()
    return rows

def get_device(device_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM devices WHERE id = ?", (device_id,)).fetchone()
    conn.close()
    return row

def add_device(name, room, ip_address, device_type):
    conn = get_connection()
    cur = conn.execute(
        "INSERT INTO devices (name, room, ip_address, device_type) VALUES (?, ?, ?, ?)",
        (name, room, ip_address, device_type),
    )
    conn.commit()
    device_id = cur.lastrowid
    conn.close()
    return device_id

def update_power(device_id, state):
    conn = get_connection()
    conn.execute("UPDATE devices SET power_state = ? WHERE id = ?", (1 if state else 0, device_id))
    conn.commit()
    conn.close()

def delete_device(device_id):
    conn = get_connection()
    conn.execute("DELETE FROM devices WHERE id = ?", (device_id,))
    conn.commit()
    conn.close()

def list_automations():
    conn = get_connection()
    rows = conn.execute(
        "SELECT a.*, d.name AS device_name FROM automations a JOIN devices d ON d.id = a.device_id ORDER BY a.id DESC"
    ).fetchall()
    conn.close()
    return rows

def add_automation(name, device_id, trigger_state, action_state):
    conn = get_connection()
    conn.execute(
        "INSERT INTO automations (name, device_id, trigger_state, action_state) VALUES (?, ?, ?, ?)",
        (name, device_id, trigger_state, action_state),
    )
    conn.commit()
    conn.close()
