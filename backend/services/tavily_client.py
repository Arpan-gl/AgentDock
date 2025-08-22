import requests
from app_settings import settings

def search(query: str, depth="advanced"):
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {settings.TAVILY_API_KEY}"}
    payload = {"query": query, "search_depth": depth}
    resp = requests.post(url, json=payload, headers=headers, timeout=15)
    resp.raise_for_status()
    return resp.json()

def extract(url: str):
    url_ = "https://api.tavily.com/extract"
    headers = {"Authorization": f"Bearer {settings.TAVILY_API_KEY}"}
    payload = {"url": url}
    resp = requests.post(url_, json=payload, headers=headers, timeout=15)
    resp.raise_for_status()
    return resp.json()
