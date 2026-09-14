import os
from flask import Flask
from pyrogram import Client, filters
import threading

# 1. إعداد خادم Flask البسيط لمنع المنصة من إغلاق البوت
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "UserBot is running and active!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    # نوقف استخدام الـ reloader لمنع التعارض مع بايثون
    app_flask.run(host="0.0.0.0", port=port, use_reloader=False)

# تشغيل الفلاسك في خلفية منفصلة
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

# 2. بيانات Pyrogram
API_ID = 6
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

SOURCE_CHANNELS = [
    "pdf_books2u",
    "syriaaa22",
    "books_nour",
    "books2024",
    "ilovebooks12345",
    "books2023",
    "million_2026",
    "arabickindle1",
    "art_of_book"
]
TARGET_GROUP = "@rafiq_words_group"

app = Client("my_userbot", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)

@app.on_message(filters.chat(SOURCE_CHANNELS) & (filters.document | filters.photo))
async def forward_books(client, message):
    try:
        await message.forward(TARGET_GROUP)
    except Exception as e:
        print(f"خطأ في التحويل: {e}")

if __name__ == "__main__":
    print("الـ UserBot يعمل الآن ويراقب القنوات...")
    app.run()
    
@app.on_message(filters.chat(SOURCE_CHANNELS) & (filters.document | filters.photo))
async def forward_books(client, message):
    try:
        await message.forward(TARGET_GROUP)
    except Exception as e:
        print(f"خطأ في التحويل: {e}")

if __name__ == "__main__":
    # تشغيل خادم الفلاسك في الخلفية بالتوازي مع البوت
    t = threading.Thread(target=run_flask)
    t.start()
    
    print("الـ UserBot وخادم الحماية يعملان الآن...")
    app.run()
    
