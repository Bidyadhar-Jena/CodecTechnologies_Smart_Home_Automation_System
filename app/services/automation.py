from database import get_connection, get_device, update_power
from services.tasmota import TasmotaError, set_power
from config import DEMO_MODE

def run_automations():
    conn = get_connection()
    rules = conn.execute(
        "SELECT id, device_id, trigger_state, action_state, enabled FROM automations WHERE enabled = 1"
    ).fetchall()
    conn.close()

    results = []
    for rule in rules:
        device = get_device(rule["device_id"])
        if device is None:
            continue

        current = int(device["power_state"])
        trigger = int(rule["trigger_state"])
        action = int(rule["action_state"])

        if current != trigger:
            continue

        if DEMO_MODE or not device["ip_address"]:
            update_power(device["id"], action)
            results.append({"rule_id": rule["id"], "device_id": device["id"], "mode": "demo", "state": bool(action)})
            continue

        try:
            set_power(device["ip_address"], bool(action))
            update_power(device["id"], action)
            results.append({"rule_id": rule["id"], "device_id": device["id"], "mode": "tasmota", "state": bool(action)})
        except TasmotaError as exc:
            results.append({"rule_id": rule["id"], "device_id": device["id"], "error": str(exc)})

    return results
