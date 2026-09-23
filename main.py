import random
import telebot
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

TOKEN = '8996399169:AAEAXrJc50xcopyqF5fE-lbmPSB0VrnTJtU'  # BotFather er Token
bot = telebot.TeleBot(TOKEN)

EMOJI_LIST = ['👍', '❤️', '🔥', '🎉', '🥰', '👏', '⚡', '💯']

# Proti ta new channel post e reaction dibe
@bot.channel_post_handler(func=lambda message: True)
def auto_react(message):
    try:
        selected_emoji = random.choice(EMOJI_LIST)
        bot.set_message_reaction(
            chat_id=message.chat.id,
            message_id=message.message_id,
            reaction=[telebot.types.ReactionTypeEmoji(selected_emoji)]
        )
        print(f"Reaction sent to post {message.message_id}")
    except Exception as e:
        print(f"Error giving reaction: {e}")

if __name__ == "__main__":
    keep_alive()
    # Continuous polling ensure kore jeno kono post miss na hoy
    bot.infinity_polling(timeout=20, long_polling_timeout=10)
    bot.infinity_polling()
