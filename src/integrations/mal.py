import requests
import os
import logging

MAL_CLIENT_ID = os.getenv("MAL_CLIENT_ID")
MAL_API_URL = "https://api.myanimelist.net/v2/anime"

def fetch_mal_anime(query: str):
    headers = {"X-MAL-CLIENT-ID": MAL_CLIENT_ID}
    params = {"q": query, "limit": 1}
    try:
        resp = requests.get(MAL_API_URL, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", [])[0] if data.get("data") else None
    except Exception as e:
        logging.error(f"MAL fetch error: {e}")
        return None
