from functools import wraps
from flask import request
from .utils import verify_server
from .exceptions import VerificationFailed

# internal store for verification
_verified_servers = {}

def bell_tag(server_id: str = None, api_key: str = None):
    """
    Decorator to track a Flask route.
    Automatically verifies the server on first usage.
    
    Usage:
        @app.route("/my-route")
        @bell_tag(server_id="ABC", api_key="XYZ")
        def my_route():
            return "Hello"
    """
    if server_id is None or api_key is None:
        raise VerificationFailed("server_id and api_key must be provided")

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # verify server only once
            if server_id not in _verified_servers:
                if not verify_server(server_id, api_key):
                    raise VerificationFailed("Server verification failed.")
                _verified_servers[server_id] = True

            # Track the request
            try:
                ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
                user_agent = request.headers.get('User-Agent')
                path = request.path
                method = request.method

                # Normally send to your API server
                import requests
                requests.post(
                    "https://belltagmanager.com/api/v1/track",
                    json={
                        "server_id": server_id,
                        "path": path,
                        "method": method,
                        "ip": ip_address,
                        "user_agent": user_agent
                    },
                    timeout=3
                )
            except Exception:
                pass  # fail silently

            return f(*args, **kwargs)

        return wrapper
    return decorator
