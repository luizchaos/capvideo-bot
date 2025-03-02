import telebot
import logging

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

BOT_TOKEN = ""

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True, content_types=["video", "photo", "link", "text"])
def send_message(message):
    if message.chat.id == -4799576555:
        if message.content_type == "video":
            bot.reply_to(message, message.caption)
        elif message.content_type == "text":
            bot.reply_to(message, message.text)


bot.infinity_polling()