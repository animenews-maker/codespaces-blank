import requests
from typing import List, Dict, Any, Optional
import logging
import os

REDDIT_URL = "https://www.reddit.com/r/anime/top.json?limit=5&t=day"
HEADERS = {'User-agent': os.getenv('REDDIT_USER_AGENT', 'AnimeAutopilotBot/1.0')}

def fetch_reddit_top(limit: int = 5, subreddit: str = "anime") -> Optional[List[Dict[str, Any]]]:
    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit={limit}&t=day"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['data']['children']
    except Exception as e:
        logging.error(f"Reddit fetch error: {e}")
        return None

# Add support for more subreddits and dynamic sources in the future
