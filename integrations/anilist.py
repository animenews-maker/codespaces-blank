import requests
from typing import List, Dict, Any, Optional
import logging

ANILIST_API = "https://graphql.anilist.co"

ANIME_NEWS_QUERY = '''
query ($perPage: Int) {
  Page(perPage: $perPage) {
    media(type: ANIME, sort: TRENDING_DESC) {
      id
      title { romaji english native }
      siteUrl
      coverImage { large }
      description(asHtml: false)
      genres
      averageScore
      startDate { year month day }
      studios { nodes { name } }
    }
  }
}
'''

def fetch_anime_news(per_page: int = 5) -> Optional[List[Dict[str, Any]]]:
    variables = {"perPage": per_page}
    try:
        response = requests.post(ANILIST_API, json={'query': ANIME_NEWS_QUERY, 'variables': variables}, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['data']['Page']['media']
    except Exception as e:
        logging.error(f"AniList fetch error: {e}")
        return None

def fetch_anime_by_id(anime_id: int) -> Optional[Dict[str, Any]]:
    query = '''
    query ($id: Int) {
      Media(id: $id, type: ANIME) {
        id
        title { romaji english native }
        siteUrl
        coverImage { large }
        description(asHtml: false)
        genres
        averageScore
        startDate { year month day }
        studios { nodes { name } }
      }
    }
    '''
    try:
        response = requests.post(ANILIST_API, json={'query': query, 'variables': {'id': anime_id}}, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['data']['Media']
    except Exception as e:
        logging.error(f"AniList fetch by id error: {e}")
        return None
