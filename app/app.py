from flask import Flask, jsonify, redirect, render_template, request, url_for
from config import DEBUG, DEMO_MODE, HOST, PORT
from database import add_automation, add_device, delete_device, get_device, init_db, list_automations, list_devices, update_power
from services.tasmota import TasmotaError, get_status, set_power
from services.automation import run_automations

app = Flask(__name__)
init_db()

def dashboard_stats(devices):
    return {
        "total": len(devices),
        "online": sum(int(d["online"]) for d in devices),
        "active": sum(int(d["power_state"]) for d in devices),
    }

@app.get("/")
def index():
    devices = list_devices()
    return render_template("index.html", devices=devices, stats=dashboard_stats(devices), demo_mode=DEMO_MODE)

@app.get("/devices")
def devices_page():
    return render_template("devices.html", devices=list_devices())

@app.post("/devices")
def create_device():
    name = request.form.get("name", "").strip()
    room = request.form.get("room", "").strip()
    ip_address = request.form.get("ip_address", "").strip()
    device_type = request.form.get("device_type", "Switch").strip()
    if not name or not room:
        return redirect(url_for("devices_page"))
    add_device(name, room, ip_address, device_type)
    return redirect(url_for("devices_page"))

@app.post("/devices/<int:device_id>/delete")
def remove_device(device_id):
    delete_device(device_id)
    return redirect(url_for("devices_page"))

@app.post("/api/devices/<int:device_id>/power")
def power(device_id):
    device = get_device(device_id)
    if device is None:
        return jsonify({"ok": False, "error": "Device not found"}), 404
    payload = request.get_json(silent=True) or {}
    desired = bool(payload.get("state"))
    if DEMO_MODE or not device["ip_address"]:
        update_power(device_id, desired)
        return jsonify({"ok": True, "mode": "demo", "state": desired})
    try:
        set_power(device["ip_address"], desired)
        update_power(device_id, desired)
        return jsonify({"ok": True, "mode": "tasmota", "state": desired})
    except TasmotaError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 502

@app.get("/api/devices/<int:device_id>/status")
def status(device_id):
    device = get_device(device_id)
    if device is None:
        return jsonify({"ok": False, "error": "Device not found"}), 404
    if DEMO_MODE or not device["ip_address"]:
        return jsonify({"ok": True, "mode": "demo", "state": bool(device["power_state"])})
    try:
        _, body = get_status(device["ip_address"])
        return jsonify({"ok": True, "mode": "tasmota", "raw": body})
    except TasmotaError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 502

@app.get("/automations")
def automations_page():
    return render_template("automations.html", devices=list_devices(), automations=list_automations())

@app.post("/automations")
def create_automation():
    name = request.form.get("name", "").strip()
    device_id = request.form.get("device_id", type=int)
    trigger_state = request.form.get("trigger_state", type=int)
    action_state = request.form.get("action_state", type=int)
    if name and device_id is not None:
        add_automation(name, device_id, trigger_state or 0, action_state or 0)
    return redirect(url_for("automations_page"))

@app.post("/api/automations/run")
def run_automation_rules():
    return jsonify({"ok": True, "results": run_automations()})

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "demo_mode": DEMO_MODE})

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
