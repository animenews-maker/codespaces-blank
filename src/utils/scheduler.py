import asyncio
import logging
from datetime import datetime, timedelta
from src.core.config import load_config
from src.discord_bot.bot import post_to_channels

async def start_scheduler(config):
    async def scheduler_loop():
        while True:
            try:
                await post_to_channels(config)
            except Exception as e:
                logging.exception("Scheduler error")
            await asyncio.sleep(1800)  # 30 minutes
    asyncio.create_task(scheduler_loop())
