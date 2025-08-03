from pyrogram.types import Message
from config import SHRINKME_API_KEY
import requests

user_steps = {}

def save_user_step(user_id, step):
    user_steps[user_id] = step

def get_user_step(user_id):
    return user_steps.get(user_id)

def create_shrinkme_link(original_url: str) -> str:
    res = requests.get(f"https://shrinkme.io/api?api={SHRINKME_API_KEY}&url={original_url}")
    data = res.json()
    return data.get("shortenedUrl", original_url)
