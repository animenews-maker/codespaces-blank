from flask import Flask
from threading import Thread
import logging
import os

app = Flask('')

@app.route('/')
def home():
    return "Anime Autopilot Bot is running!"

@app.route('/health')
def health():
    return "OK", 200

def run():
    try:
        port = int(os.environ.get('PORT', 8080))
        app.run(host='0.0.0.0', port=port)
    except Exception as e:
        logging.exception("Web keep_alive server failed:")

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
