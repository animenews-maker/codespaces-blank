import requests
import os
import logging

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search"

def fetch_trailers(query: str, max_results: int = 3):
    params = {
        "part": "snippet",
        "q": query + " trailer",
        "type": "video",
        "key": YOUTUBE_API_KEY,
        "maxResults": max_results
    }
    try:
        resp = requests.get(YOUTUBE_API_URL, params=params)
        resp.raise_for_status()
        items = resp.json().get("items", [])
        return [
            {
                "title": item["snippet"]["title"],
                "url": f"https://youtube.com/watch?v={item['id']['videoId']}"
            }
            for item in items
        ]
    except Exception as e:
        logging.error(f"YouTube fetch error: {e}")
        return []
