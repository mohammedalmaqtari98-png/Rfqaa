import os
from threading import Thread
from flask import Flask
import telebot

# 1. إعداد خادم Keep-Alive
app = Flask("")


@app.route("/")
def home():
  return "Bot is alive and running 24/7!"


def run():
  app.run(host="0.0.0.0", port=8080)


def keep_alive():
  t = Thread(target=run)
  t.daemon = True
  t.start()


keep_alive()

# 2. إعداد البوت
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# قنوات الكتب فقط
SOURCE_CHANNELS = [
    "pdf_books2u",
    "syriaaa22",
    "books_nour",
    "books2024",
    "ilovebooks12345",
    "books2023",
    "million_2026",
    "arabickindle1",
    "art_of_book",
]

TARGET_CHANNELS = ["@rafiq_words_group", "@wordscomp"]


# استقبال المستندات والكتب فقط (document)
@bot.channel_post_handler(content_types=["document"])
def forward_books_only(message):
  if (
      message.chat.username
      and message.chat.username.lower() in SOURCE_CHANNELS
  ):
    for target in TARGET_CHANNELS:
      try:
        bot.forward_message(target, message.chat.id, message.message_id)
        print(f"تم توجيه الكتاب بنجاح إلى {target}")
      except Exception as e:
        print(f"خطأ أثناء التوجيه: {e}")


print("بوت توجيه الكتب متصل ويعمل...")
bot.infinity_polling()
