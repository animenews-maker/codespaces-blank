import json
import os
from datetime import datetime
from typing import Dict, Any

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../../config/config.json')
BACKUP_DIR = os.path.join(os.path.dirname(__file__), '../../config/')

REQUIRED_KEYS = ["channels", "sources", "dashboard", "backup"]


def check_config() -> Dict[str, Any]:
    with open(CONFIG_PATH) as f:
        config = json.load(f)
    missing = [k for k in REQUIRED_KEYS if k not in config]
    return {"missing": missing}


def backup_config() -> str:
    now = datetime.now().strftime('%Y-%m-%d')
    backup_path = os.path.join(BACKUP_DIR, f"config_backup_{now}.json")
    with open(CONFIG_PATH) as f:
        data = f.read()
    with open(backup_path, 'w') as f:
        f.write(data)
    return backup_path


def diff_config() -> str:
    backups = [f for f in os.listdir(BACKUP_DIR) if f.startswith('config_backup_')]
    if not backups:
        return "No backups found."
    backups.sort(reverse=True)
    latest = backups[0]
    with open(CONFIG_PATH) as f:
        current = f.readlines()
    with open(os.path.join(BACKUP_DIR, latest)) as f:
        backup = f.readlines()
    import difflib
    diff = difflib.unified_diff(backup, current, fromfile=latest, tofile='config.json')
    return '\n'.join(diff)


def restore_config(date: str) -> str:
    backup_path = os.path.join(BACKUP_DIR, f"config_backup_{date}.json")
    if not os.path.exists(backup_path):
        return "Backup not found."
    with open(backup_path) as f:
        data = f.read()
    with open(CONFIG_PATH, 'w') as f:
        f.write(data)
    return "Config restored."
