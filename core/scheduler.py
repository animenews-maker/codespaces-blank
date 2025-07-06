from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import logging
from typing import Any, Dict, Callable

scheduler = None

def start_scheduler(config: Dict[str, Any], post_jobs: Dict[str, Callable] = None):
    global scheduler
    scheduler = BackgroundScheduler()
    bot_settings = config.get("bot_settings", {})
    short_interval = bot_settings.get("update_interval_minutes_short", 30)
    long_interval = bot_settings.get("update_interval_hours_long", 24)

    # Register jobs for all sources if provided
    if post_jobs:
        for job_name, job_func in post_jobs.items():
            if job_name == "short":
                scheduler.add_job(job_func, IntervalTrigger(minutes=short_interval), id="short_job", replace_existing=True)
            elif job_name == "long":
                scheduler.add_job(job_func, IntervalTrigger(hours=long_interval), id="long_job", replace_existing=True)
            else:
                # Custom jobs for new sources
                scheduler.add_job(job_func, IntervalTrigger(minutes=short_interval), id=job_name, replace_existing=True)

    scheduler.start()
    logging.info(f"Scheduler started with intervals: short={short_interval}min, long={long_interval}h.")

def stop_scheduler():
    global scheduler
    if scheduler:
        scheduler.shutdown()
        logging.info("Scheduler stopped.")
