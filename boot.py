import os
import requests
import telebot
from dotenv import load_dotenv
from telebot import types

# تحميل المتغيرات من ملف .env
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
LOGIN_URL = "https://social.trendatelyoum.com/login"
ADD_CARD_URL = "https://social.trendatelyoum.com/MedozTools/addcardamexmulti/"

bot = telebot.TeleBot(TOKEN)
session = requests.Session()

# دالة تسجيل الدخول
def login():
    data = {"username": USERNAME, "password": PASSWORD}
    response = session.post(LOGIN_URL, data=data)
    return "تم تسجيل الدخول بنجاح" if response.ok else f"فشل في تسجيل الدخول. حالة الاستجابة: {response.status_code}"

# أمر /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    login_button = types.InlineKeyboardButton("تسجيل الدخول", callback_data="login")
    add_card_button = types.InlineKeyboardButton("إضافة بطاقة", callback_data="add_card")
    markup.add(login_button, add_card_button)
    
    bot.reply_to(message, "مرحبًا! اختر إحدى الخيارات:", reply_markup=markup)

# دالة الرد على أمر /login
@bot.message_handler(commands=['login'])
def login_command(message):
    result = login()
    bot.reply_to(message, result)

# دالة الرد على أمر /addcard
@bot.message_handler(commands=['addcard'])
def add_card(message):
    card_data = {"card_number": "123456789"}  # غيّرها حسب الحاجة
    response = session.post(ADD_CARD_URL, data=card_data)
    result = "تمت إضافة البطاقة بنجاح!" if response.ok else f"فشل في إضافة البطاقة. حالة الاستجابة: {response.status_code}"
    bot.reply_to(message, result)

# التعامل مع الأزرار المدمجة
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "login":
        result = login()
        bot.answer_callback_query(call.id, result)
    elif call.data == "add_card":
        card_data = {"card_number": "123456789"}  # غيّرها حسب الحاجة
        response = session.post(ADD_CARD_URL, data=card_data)
        result = "تمت إضافة البطاقة بنجاح!" if response.ok else f"فشل في إضافة البطاقة. حالة الاستجابة: {response.status_code}"
        bot.answer_callback_query(call.id, result)

# تشغيل البوت
bot.polling()
