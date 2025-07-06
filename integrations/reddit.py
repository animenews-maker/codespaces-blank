import requests

REDDIT_URL = "https://www.reddit.com/r/anime/top.json?limit=5&t=day"

headers = {'User-agent': 'AnimeAutopilotBot/0.1'}

def fetch_reddit_top():
    response = requests.get(REDDIT_URL, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['children']
    return []
