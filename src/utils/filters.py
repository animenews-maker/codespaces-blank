import hashlib

def is_duplicate(post_id: str, recent_ids: list) -> bool:
    return post_id in recent_ids

def hash_content(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()
