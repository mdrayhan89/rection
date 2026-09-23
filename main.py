import random
import telebot
from flask import Flask
from threading import Thread

# Flask Server Setup
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

# Telegram Bot Setup
TOKEN = '8772565875:AAHyDH-063rlJoEoO5vvrEVnUtRQoTsHIdA'
bot = telebot.TeleBot(TOKEN)

# যে ইমোজিগুলো থেকে বট বেছে নেবে তার একটি তালিকা
EMOJI_LIST = ['👍', '❤️', '🔥', '🎉', '🥰', '👏', '⚡', '💯']

@bot.channel_post_handler(func=lambda message: True)
def auto_react(message):
    try:
        # তালিকা থেকে যেকোনো একটি ইমোজি এলোমেলোভাবে সিলেক্ট করা
        selected_emoji = random.choice(EMOJI_LIST)
        
        bot.set_message_reaction(
            chat_id=message.chat.id,
            message_id=message.message_id,
            reaction=[telebot.types.ReactionTypeEmoji(selected_emoji)]
        )
        print(f"Post {message.message_id}-এ '{selected_emoji}' রিঅ্যাকশন দেওয়া হয়েছে!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
