import requests
import logging

ANN_API_URL = "https://cdn.animenewsnetwork.com/encyclopedia/api.xml"

def fetch_ann_news():
    try:
        resp = requests.get(ANN_API_URL)
        resp.raise_for_status()
        return resp.text  # XML parsing needed for real use
    except Exception as e:
        logging.error(f"ANN fetch error: {e}")
        return None
