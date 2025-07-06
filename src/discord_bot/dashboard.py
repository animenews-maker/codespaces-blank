from fastapi import FastAPI
import uvicorn
import threading
import os
import json

app = FastAPI()

@app.get("/dashboard")
def dashboard():
    config_path = os.path.join(os.path.dirname(__file__), '../../config/config.json')
    with open(config_path) as f:
        config = json.load(f)
    return config

def start_dashboard():
    thread = threading.Thread(target=uvicorn.run, args=(app,), kwargs={"host": "0.0.0.0", "port": 8080})
    thread.daemon = True
    thread.start()
