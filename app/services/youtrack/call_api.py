import requests
from requests.structures import CaseInsensitiveDict

from app.config import Config

BASE_URL = Config.YOUTRACK_BASE_URL
BEARER_TOKEN = Config.YOUTRACK_TOKEN
YOUTRACK_QUERY_FIELDS = Config.YOUTRACK_QUERY_FIELDS


def get(query_url: str):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer " + BEARER_TOKEN

    response = requests.get(f"{BASE_URL}{query_url}", headers=headers)

    if response.status_code == 200:
        return response.json()["issues"]
    raise RuntimeError(
        f"HTTP Status {response.status_code} - {response.json()['error']}"
    )


def url(query_id: str):
    return f"/savedQueries/{query_id}?fields=" + YOUTRACK_QUERY_FIELDS
