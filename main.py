from keep_alive import keep_alive
keep_alive()
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN, MOVIE_CHANNEL
from movie_fetcher import search_movie
from helper import save_user_step, get_user_step
from shrinkme import get_verification_link

bot = Client("rozibot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(_, msg):
    await msg.reply("🎬 Welcome! Send any movie name to search.")

@bot.on_message(filters.private & filters.text & ~filters.command("start"))
async def movie_search(_, msg):
    query = msg.text
    save_user_step(msg.from_user.id, query)
    response = await search_movie(query)
    
    await msg.reply(
        text=response.text if response.text else "Movie found.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔗 Get Link", callback_data="get_link")]
        ])
    )

@bot.on_callback_query(filters.regex("get_link"))
async def get_link(_, query):
    user_id = query.from_user.id
    movie_name = get_user_step(user_id)
    link = get_verification_link(user_id)
    
    await query.message.reply(
        f"Click below to verify and get your movie:\n\n🎬 **{movie_name}**",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ Verify & Get Link", url=link)]
        ])
    )

bot.run()
