import os
import telebot

# إبقاء التوكن مخفياً عن GitHub
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
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
