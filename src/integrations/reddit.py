import asyncpraw
import os
import logging

async def get_reddit_client():
    return asyncpraw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

async def fetch_subreddit_posts(subreddit: str, limit: int = 5):
    reddit = await get_reddit_client()
    try:
        posts = []
        async for post in reddit.subreddit(subreddit).hot(limit=limit):
            posts.append({
                "title": post.title,
                "url": post.url,
                "id": post.id
            })
        return posts
    except Exception as e:
        logging.error(f"Reddit fetch error: {e}")
        return []
