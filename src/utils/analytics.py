import logging
from src.core.db import get_recent_posts

async def get_post_stats(channel: str):
    posts = await get_recent_posts(channel)
    return {
        "count": len(posts),
        "latest": posts[0] if posts else None
    }
