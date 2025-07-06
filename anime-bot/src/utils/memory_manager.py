import json
import os
from typing import Dict, Any

MEMORY_DIR = os.path.join(os.path.dirname(__file__), '../../memory')

def get_user_memory(user_id: int) -> Dict[str, Any]:
    path = os.path.join(MEMORY_DIR, f'user_{user_id}.json')
    if not os.path.exists(path):
        return {}
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def save_user_memory(user_id: int, data: Dict[str, Any]):
    path = os.path.join(MEMORY_DIR, f'user_{user_id}.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
