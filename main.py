import telebot
from flask import Flask
from threading import Thread

# سيرفر خفيف لإبقاء الخدمة نشطة على Render
app = Flask('')

@app.route('/')
def home():
    return "Bot is Alive and Running 24/7!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

# التوكن المباشر للبوت
TOKEN = "8646517225:AAFJNmFnmycaCiZAeLd33OZrXGs8MgZAdzg"
bot = telebot.TeleBot(TOKEN)

SOURCE_CHANNELS = [
    "art_of_book",
    "riwayattime",
    "katabatakatabata",
    "books2023",
    "million_2026"
]

TARGET_CHANNELS = [
    "@rafiq_words_group",
    "@wordscomp"
]

@bot.channel_post_handler(func=lambda message: True)
def auto_forward(message):
    if message.chat.username and message.chat.username.lower() in SOURCE_CHANNELS:
        for target in TARGET_CHANNELS:
            try:
                bot.forward_message(target, message.chat.id, message.message_id)
                print(f"تم التوجيه بنجاح إلى {target}")
            except Exception as e:
                print(f"خطأ أثناء التوجيه إلى {target}: {e}")

if __name__ == "__main__":
    keep_alive()  # تشغيل خادم الحفاظ على النشاط
    print("البوت متصل بالسيرفر ويعمل بنجاح...")
    bot.infinity_polling()
