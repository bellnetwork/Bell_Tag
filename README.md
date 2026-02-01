# Bell Tag

[![PyPI version](https://img.shields.io/pypi/v/bell_tag)](https://pypi.org/project/bell_tag/)
[![Python Version](https://img.shields.io/pypi/pyversions/bell_tag)](https://pypi.org/project/bell_tag/)
[![License](https://img.shields.io/pypi/l/bell_tag)](https://opensource.org/licenses/MIT)

**Bell Tag** is a lightweight, secure, and modern Python analytics tracking library for Flask applications.  
It allows you to track page views, events, clicks, forms, and user navigation **without exposing credentials**. Verification happens automatically on first usage.

This package is developed and maintained by **Bell Network** ([bellnetwork.eu](https://bellnetwork.eu)).  
Users can manage their servers, view analytics, and configure settings on the dashboard at [dash.bellnetwork.eu](https://dash.bellnetwork.eu).

---

## Features

- Automatic user/session tracking in Flask routes
- Decorator `@bell_tag` to enable tracking on any route
- Tracks:
  - Page views
  - Click events
  - Form submissions
  - Scroll depth
  - Navigation between routes
- All events are sent **securely to Bell Network servers** and stored in our database
- Fully encrypted data transfer over HTTPS
- Access to analytics is restricted and private—**only authorized users can view their data**
- Fully configurable server-side verification (server ID and API key handled behind the scenes)
- Works out-of-the-box with Flask
- No credentials required during installation
- Server management and analytics available via [dash.bellnetwork.eu](https://dash.bellnetwork.eu)

---

## Data Handling & Security

Bell Tag takes user privacy and data security seriously:

1. **Encrypted Transfer** – All event data is sent via HTTPS with TLS 1.2+.
2. **Secure Storage** – Data is stored in Bell Network’s secure database with encryption at rest.
3. **User Access Control** – Only the owner of a server can view analytics data associated with it.
4. **Minimal Exposure** – No sensitive credentials are stored in your application.
5. **Integrity Checks** – Automatic verification ensures that data is only accepted from authorized servers.

> This ensures that your analytics are both **private** and **tamper-proof**.

---

## Installation

```bash
pip install bell_tag
