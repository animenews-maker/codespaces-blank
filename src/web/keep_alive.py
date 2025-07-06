from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK"

def start_web(config):
    port = config.get("dashboard", {}).get("port", 8080)
    thread = threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": port})
    thread.daemon = True
    thread.start()
