import requests
import logging

MANGADEX_API_URL = "https://api.mangadex.org/manga"

def fetch_manga(title: str):
    params = {"title": title, "limit": 1}
    try:
        resp = requests.get(MANGADEX_API_URL, params=params)
        resp.raise_for_status()
        data = resp.json()
        return data["data"][0] if data.get("data") else None
    except Exception as e:
        logging.error(f"MangaDex fetch error: {e}")
        return None
