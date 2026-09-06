import os
import time
from flask import Flask
import telebot

# بيانات البوت الجديد
TOKEN = "8646517225:AAEv8du-46beAhA9jvNNF2GTxUdkgozDSlM"
bot = telebot.TeleBot(TOKEN)

# معرفات القنوات المستهدفة للتحويل إليها
TARGET_CHANNELS = ["@rafiq_words_group", "@wordscomp"]

# يوزرات قنوات المصدر (بدون علامة @)
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

app = Flask(__name__)


@app.route("/")
def home():
    return "Bot is active and running!"


# استقبال الرسائل أو الملفات التي يتم توجيهها أو وصولها
@bot.message_handler(content_types=["document", "file"])
def handle_docs(message):
    # التأكد أن الرسالة أو الملف يخص الكتب أو من القنوات المسموحة
    try:
        for target in TARGET_CHANNELS:
            bot.forward_message(
                chat_id=target,
                from_chat_id=message.chat.id,
                message_id=message.message_id,
            )
        print("تم تحويل الكتاب بنجاح!")
    except Exception as e:
        print(f"خطأ أثناء التوجيه: {e}")


if __name__ == "__main__":
    # تشغيل سيرفر Flask لضمان عدم نوم البوت على Render
    port = int(os.environ.get("PORT", 5000))

    # تشغيل البوت بوضع البوليغ المستمر
    import threading

    def run_bot():
        while True:
            try:
                print("Bot is polling...")
                bot.infinity_polling(skip_pending=True)
            except Exception as e:
                print(f"Polling error: {e}")
                time.sleep(5)

    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    app.run(host="0.0.0.0", port=port)
  
