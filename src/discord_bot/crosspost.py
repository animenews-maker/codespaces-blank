from src.integrations.twitter import post_to_twitter

async def crosspost_to_all(text: str, image_path: str = None):
    # Twitter
    post_to_twitter(text, image_path)
    # Add Telegram, Threads, Instagram, etc. here
