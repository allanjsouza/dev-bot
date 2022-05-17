import requests

from app.models.shouldideploy import ShouldideployMessage

SERVICE_NAME = "shouldideploy.today"
SERVICE_URL = "https://shouldideploy.today"
SERVICE_ENDPOINT = "/api/slack?tz=Etc/GMT-3"


def get_service_name():
    return SERVICE_NAME


def get_service_url():
    return SERVICE_URL


def check_shouldideploy() -> ShouldideployMessage:
    response = requests.get(SERVICE_URL + SERVICE_ENDPOINT)
    if response.ok:
        json_response = response.json()
        [msg] = json_response.get("attachments")
        result = ShouldideployMessage(msg.get("text"))
        result.color = msg.get("color")
        result.thumb_url = msg.get("thumb_url")
        result.footer = msg.get("footer")
        result.footer_icon = msg.get("footer_icon")
        return result
    raise RuntimeError(f"HTTP Status {response.status_code} - {response.raw}")
