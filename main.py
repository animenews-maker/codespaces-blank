# main.py
# Entry point for Anime Autopilot Discord Bot

import logging
import sys
import signal
import asyncio
from core.config import load_config
from core.db import run_init_db
from core.scheduler import start_scheduler
from discord.bot import start_discord_bot
from web.keep_alive import keep_alive
from datetime import datetime


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s:%(name)s: %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    logging.getLogger('discord').setLevel(logging.WARNING)
    logging.getLogger('apscheduler').setLevel(logging.WARNING)
    logging.info(f"Logging initialized at {datetime.now().isoformat()}")


def shutdown_handler(signum, frame):
    logging.info(f"Received signal {signum}. Shutting down gracefully...")
    sys.exit(0)


def main():
    setup_logging()
    logging.info("Starting Anime Autopilot Discord Bot...")
    config = load_config()
    run_init_db()
    keep_alive()
    start_scheduler(config)
    start_discord_bot(config)

if __name__ == "__main__":
    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, shutdown_handler)
    try:
        main()
    except Exception as e:
        logging.exception("Fatal error in main loop:")
        sys.exit(1)
