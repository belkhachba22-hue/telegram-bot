import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8681921752:AAHMquwqFkhTlY1Iof4xx1WS4W-0_MBCuVM"

bot = telebot.TeleBot(TOKEN)

users = {}

def menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🚀 Signal", "💎 VIP")
    markup.row("📊 My Account", "📞 Support")
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    users[user_id] = {"vip": False}
    
    bot.send_message(
        user_id,
        "🔥 مرحبا بك في بوت Aviator Predictor\n\nاختر من القائمة 👇",
        reply_markup=menu()
    )

@bot.message_handler(func=lambda message: True)
def handle(message):
    user_id = message.chat.id
    text = message.text

    if text == "🚀 Signal":
        if users.get(user_id, {}).get("vip"):
            bot.send_message(user_id, "📊 Signal: 2.35x 🔥")
        else:
            bot.send_message(user_id, "❌ هذه الميزة VIP فقط")

    elif text == "💎 VIP":
        bot.send_message(user_id, "💰 للاشتراك راسل الدعم")

    elif text == "📊 My Account":
        status = "VIP" if users.get(user_id, {}).get("vip") else "Free"
        bot.send_message(user_id, f"📌 حسابك: {status}")

    elif text == "📞 Support":
        bot.send_message(user_id, "📩 تواصل مع الادمن: @username")

bot.infinity_polling()
