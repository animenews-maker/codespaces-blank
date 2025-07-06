import requests
import logging

ANILIST_API = "https://graphql.anilist.co"

def fetch_anime(title: str):
    query = '''
    query ($search: String) {
      Media(search: $search, type: ANIME) {
        id
        title { romaji english native }
        coverImage { large }
        description
        averageScore
        genres
        studios { nodes { name } }
        season
        siteUrl
      }
    }
    '''
    variables = {"search": title}
    try:
        response = requests.post(ANILIST_API, json={"query": query, "variables": variables})
        response.raise_for_status()
        return response.json()["data"]["Media"]
    except Exception as e:
        logging.error(f"AniList fetch error: {e}")
        return None
