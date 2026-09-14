import os
import threading
from flask import Flask
from pyrogram import Client, filters

# 1. إعداد خادم Flask البسيط لمنع السبات
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "UserBot is running and active!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app_flask.run(host="0.0.0.0", port=port, use_reloader=False)

flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

# 2. بيانات Pyrogram
API_ID = 6
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

# نقرأ رقم الهاتف أو الجلسة من متغيرات البيئة
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
SESSION_STRING = os.environ.get("SESSION_STRING") # خيار إضافي مستقبلي

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

# إذا متوفرة الجلسة يستخدمها، وإلا يبدأ برقم الهاتف
if SESSION_STRING:
    app = Client("my_userbot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
else:
    app = Client("my_userbot", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)

@app.on_message(filters.chat(SOURCE_CHANNELS) & (filters.document | filters.photo))
async def forward_books(client, message):
    try:
        await message.forward(TARGET_GROUP)
    except Exception as e:
        print(f"خطأ في التحويل: {e}")

if __name__ == "__main__":
    print("جاري تشغيل الـ UserBot...")
    app.run()
    
