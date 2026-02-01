import requests
import socket
from .constants import API_URL, DEFAULT_TIMEOUT

def get_local_ip():
    """Try to get the server's external IP address"""
    try:
        return requests.get("https://api.ipify.org", timeout=2).text
    except requests.RequestException:
        return "127.0.0.1"

def verify_server(server_id: str, api_key: str):
    """
    Verify server with Bell API.
    Returns True if verified, False otherwise
    """
    try:
        ip = get_local_ip()
        response = requests.post(
            API_URL,
            json={"server_id": server_id, "api_key": api_key, "ip": ip},
            timeout=DEFAULT_TIMEOUT
        )
        data = response.json()
        return data.get("status") == "ok"
    except Exception:
        return False
