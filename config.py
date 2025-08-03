import os

API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
SHRINKME_API_KEY = os.getenv("SHRINKME_API_KEY", "your_shrinkme_api_key")

SESSION_STRING = os.getenv("SESSION_STRING", "your_pyrogram_string_session")

MOVIE_SOURCE_BOT = "CARZYHUBXBOT"  # Corrected bot
MOVIE_CHANNEL = "@rozimovie"  # Where bot sends the final movie
