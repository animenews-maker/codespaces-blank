import requests
import logging

ANICHART_API_URL = "https://anichart.net/api/season"

def fetch_anichart_season(season: str, year: int):
    try:
        resp = requests.get(f"{ANICHART_API_URL}/{year}/{season}")
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        logging.error(f"AniChart fetch error: {e}")
        return None
