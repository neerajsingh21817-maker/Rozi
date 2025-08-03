from pyrogram import Client
from config import SESSION_STRING, API_ID, API_HASH, MOVIE_SOURCE_BOT
from pyrogram.types import Message
import asyncio

client = Client("movie-fetcher", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

async def search_movie(query):
    await client.connect()
    async with client.conversation(MOVIE_SOURCE_BOT, timeout=30) as conv:
        await conv.send_message(query)
        response = await conv.get_response()
    await client.disconnect()
    return response
