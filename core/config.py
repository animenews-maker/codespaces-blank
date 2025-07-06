import json
import os
from typing import Any, Dict

CONFIG_PATH = os.getenv("ANIME_BOT_CONFIG", "config.json")

class ConfigError(Exception):
    pass

def load_config(path: str = CONFIG_PATH) -> Dict[str, Any]:
    if not os.path.exists(path):
        raise ConfigError(f"Config file not found: {path}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            config = json.load(f)
        # Basic validation
        if "bot_settings" not in config or "channels" not in config:
            raise ConfigError("Missing required keys in config.json")
        return config
    except json.JSONDecodeError as e:
        raise ConfigError(f"Invalid JSON in config file: {e}")
