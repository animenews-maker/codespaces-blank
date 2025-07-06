import json
import os
from typing import Dict, Any

CONTRIB_DIR = os.path.join(os.path.dirname(__file__), '../../contributions')

def add_contribution(user_id: int, data: Dict[str, Any]):
    path = os.path.join(CONTRIB_DIR, f'user_{user_id}.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            contribs = json.load(f)
    else:
        contribs = []
    contribs.append(data)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(contribs, f, ensure_ascii=False, indent=2)

def get_contributions(user_id: int):
    path = os.path.join(CONTRIB_DIR, f'user_{user_id}.json')
    if not os.path.exists(path):
        return []
    with open(path, encoding='utf-8') as f:
        return json.load(f)
