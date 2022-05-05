import requests

from app.models.quote import Quote

SERVICE_NAME = "zenquotes.io"
SERVICE_URL = "https://zenquotes.io/api/random"


def get_service_name():
    return SERVICE_NAME


def get_random_quote():
    response = requests.get(SERVICE_URL)
    if response.ok:
        [random_quote] = response.json()
        return Quote(random_quote.get("q"), random_quote.get("a"))
    raise RuntimeError(f"HTTP Status {response.status_code} - {response.raw}")
