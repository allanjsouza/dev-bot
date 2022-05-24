import requests
from requests.structures import CaseInsensitiveDict
from app.config import Config


def get(query_url):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer " + Config.YOUTRACK_TOKEN

    results = requests.get(Config.YOUTRACK_BASE_URL +
                           query_url, headers=headers).json()

    return results["issues"]


def url(query_id):
    return f"/savedQueries/{query_id}?fields=issues(idReadable,id,created,resolved,summary,customFields(name,value(name)),project(name))"
