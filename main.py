import os
from threading import Thread
from flask import Flask
import telebot

# 1. إعداد خادم Keep-Alive لمنع البوت من النوم
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


# تشغيل خادم الحفاظ على النشاط فوراً
keep_alive()

# 2. إعداد وقراءة توكن البوت من Render
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# القنوات المصدر
SOURCE_CHANNELS = [
    "art_of_book",
    "riwayattime",
    "katabatakatabata",
    "books2023",
    "million_2026",
]

# القنوات الهدف
TARGET_CHANNELS = ["@rafiq_words_group", "@wordscomp"]


@bot.channel_post_handler(func=lambda message: True)
def auto_forward(message):
  if (
      message.chat.username
      and message.chat.username.lower() in SOURCE_CHANNELS
  ):
    for target in TARGET_CHANNELS:
      try:
        bot.forward_message(target, message.chat.id, message.message_id)
        print(f"تم التوجيه بنجاح إلى {target}")
      except Exception as e:
        print(f"خطأ أثناء التوجيه إلى {target}: {e}")


print("البوت متصل بالسيرفر ويعمل بنجاح...")
bot.infinity_polling()
