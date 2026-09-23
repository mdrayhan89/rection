import random
import asyncio
from flask import Flask
from threading import Thread
from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji

# Flask Server Setup (Render-কে ২৪/৭ জাগিয়ে রাখার জন্য)
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

# API Credentials (my.telegram.org থেকে নেওয়া)
API_ID = 38101204  # আপনার Integer API ID বসান
API_HASH = 'db2533c8aa466bae30e453e7f0f15910'  # আপনার API Hash বসান
BOT_TOKEN = '8996399169:AAEAXrJc50xcopyqF5fE-lbmPSB0VrnTJtU'  # BotFather থেকে পাওয়া Token

# পছন্দনীয় ইমোজির তালিকা
EMOJI_LIST = ['👍', '❤️', '🔥', '🎉', '🥰', '👏', '⚡', '💯']

client = TelegramClient('bot_session', API_ID, API_HASH)

@client.on(events.NewMessage())
async def auto_react(event):
    # শুধু চ্যানেল বা গ্রুপে আসা মেসেজ প্রসেস করবে
    if event.is_channel or event.is_group:
        try:
            # Telegram API Block এড়াতে ১ সেকেন্ডের বিরতি (Delay)
            await asyncio.sleep(1)
            
            selected_emoji = random.choice(EMOJI_LIST)
            
            await client(SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                reaction=[ReactionEmoji(emoticon=selected_emoji)]
            ))
            print(f"Post {event.id}-এ '{selected_emoji}' রিঅ্যাকশন দেওয়া হয়েছে!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    keep_alive()
    client.start(bot_token=BOT_TOKEN)
    client.run_until_disconnected()
