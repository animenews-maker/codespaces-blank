from apscheduler.schedulers.background import BackgroundScheduler
import time

def start_scheduler(config):
    scheduler = BackgroundScheduler()
    # Example: scheduler.add_job(post_news, 'interval', minutes=config["interval_minutes"])
    scheduler.start()
    print("Scheduler started.")
