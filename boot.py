import os
import requests
import telebot
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN") USERNAME = os.getenv("USERNAME") PASSWORD = os.getenv("PASSWORD") LOGIN_URL = "https://social.trendatelyoum.com/login" ADD_CARD_URL = "https://social.trendatelyoum.com/MedozTools/addcardamexmulti/"

bot = telebot.TeleBot(TOKEN) session = requests.Session()

دالة تسجيل الدخول

def login(): data = {"username": USERNAME, "password": PASSWORD} response = session.post(LOGIN_URL, data=data) return "تم تسجيل الدخول بنجاح" if response.ok else f"فشل في تسجيل الدخول. حالة الاستجابة: {response.status_code}"

أمر /start

@bot.message_handler(commands=['start']) def start(message): bot.reply_to(message, "مرحبًا! أرسل /login لتسجيل الدخول للموقع.")

أمر /login

@bot.message_handler(commands=['login']) def login_command(message): result = login() bot.reply_to(message, result)

أمر /addcard

@bot.message_handler(commands=['addcard']) def add_card(message): card_data = {"card_number": "123456789"}  # غيّرها حسب الحاجة response = session.post(ADD_CARD_URL, data=card_data) result = "تمت إضافة البطاقة بنجاح!" if response.ok else f"فشل في إضافة البطاقة. حالة الاستجابة: {response.status_code}" bot.reply_to(message, result)

تشغيل البوت

bot.polling()
