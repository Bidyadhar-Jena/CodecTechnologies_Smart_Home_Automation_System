from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from config import REQUEST_TIMEOUT

class TasmotaError(Exception):
    pass

def send_command(ip_address, command):
    if not ip_address:
        raise TasmotaError("No Tasmota IP address configured.")
    url = "http://{}/cm?{}".format(ip_address.strip(), urlencode({"cmnd": command}))
    try:
        with urlopen(url, timeout=REQUEST_TIMEOUT) as response:
            body = response.read().decode("utf-8", errors="replace")
            return response.status, body
    except (URLError, HTTPError, TimeoutError) as exc:
        raise TasmotaError(str(exc)) from exc

def set_power(ip_address, state):
    return send_command(ip_address, "Power1 On" if state else "Power1 Off")

def get_status(ip_address):
    return send_command(ip_address, "Status 0")
