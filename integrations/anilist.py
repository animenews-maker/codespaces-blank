import requests

ANILIST_API = "https://graphql.anilist.co"

def fetch_anime_news():
    query = '{ Page(perPage: 5) { media(type: ANIME, sort: TRENDING_DESC) { id title { romaji } siteUrl } } }'
    response = requests.post(ANILIST_API, json={'query': query})
    if response.status_code == 200:
        return response.json()['data']['Page']['media']
    return []
