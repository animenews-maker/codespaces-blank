import json
import os
from typing import Any, Dict

def load_config() -> Dict[str, Any]:
    config_path = os.path.join(os.path.dirname(__file__), '../../config/config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config
