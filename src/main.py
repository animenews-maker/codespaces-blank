import asyncio
from src.core.config import load_config
from src.core.db import init_db
from src.discord_bot.bot import run_discord_bot
from src.utils.scheduler import start_scheduler
from src.web.keep_alive import start_web
import logging
import os

logging.basicConfig(level=logging.INFO)

async def main():
    config = load_config()
    await init_db()
    await start_scheduler(config)
    await start_web(config)
    await run_discord_bot(config)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logging.exception("Fatal error in main loop")
