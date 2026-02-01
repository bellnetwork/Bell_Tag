API_URL = "https://belltagmanager.com/api/v1/verify_server"
DEFAULT_TIMEOUT = 5  # seconds
PACKAGE_NAME = "bell_tag"
PACKAGE_VERSION = "1.0.0"
SDK_VERSION = f"{PACKAGE_NAME}/{PACKAGE_VERSION}"
HEADERS = {
    "User-Agent": SDK_VERSION,
    "Content-Type": "application/json"
}
EVENT_TYPES = {
    "PAGE_VIEW": "page_view",
    "CLICK": "click",
    "FORM_SUBMIT": "form_submit",
    "CUSTOM_EVENT": "custom_event"
}