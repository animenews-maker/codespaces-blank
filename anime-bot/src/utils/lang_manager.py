import json
import os
from typing import Dict

LANG_DIR = os.path.join(os.path.dirname(__file__), '../../lang')

class LangManager:
    def __init__(self, lang_code: str = 'en'):
        self.lang_code = lang_code
        self.translations = self.load_lang(lang_code)

    def load_lang(self, lang_code: str) -> Dict[str, str]:
        path = os.path.join(LANG_DIR, f'{lang_code}.json')
        if not os.path.exists(path):
            path = os.path.join(LANG_DIR, 'en.json')
        with open(path, encoding='utf-8') as f:
            return json.load(f)

    def t(self, key: str, **kwargs) -> str:
        text = self.translations.get(key, key)
        return text.format(**kwargs)
