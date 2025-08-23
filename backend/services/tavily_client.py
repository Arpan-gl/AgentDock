import requests
from app_settings import settings

def extract(url: str):
    url_ = "https://api.tavily.com/extract"
    headers = {"Authorization": f"Bearer {settings.TAVILY_API_KEY}"}
    payload = {"url": url}
    resp = requests.post(url_, json=payload, headers=headers, timeout=15)
    resp.raise_for_status()
    return resp.json()
