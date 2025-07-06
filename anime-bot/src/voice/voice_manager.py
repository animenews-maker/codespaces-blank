import json
import os

VOICE_CONFIG = os.path.join(os.path.dirname(__file__), '../../voice/voices.json')

def get_voice(character: str = 'default') -> str:
    with open(VOICE_CONFIG, encoding='utf-8') as f:
        voices = json.load(f)
    return voices['characters'].get(character, voices['default'])

# Add TTS and audio playback logic here (stub)
def speak(text: str, character: str = 'default'):
    voice = get_voice(character)
    # Integrate with TTS API here
    return f"[AUDIO:{voice}] {text}"
