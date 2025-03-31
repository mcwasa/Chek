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
FACEBOOK_COOKIES = os.getenv("FACEBOOK_COOKIES")  # احفظ الكوكيز هنا
AD_ACCOUNT_ID = os.getenv("AD_ACCOUNT_ID")  # احفظ آيدي الحساب الإعلاني هنا

bot = telebot.TeleBot(TOKEN)
session = requests.Session()

# إضافة الكوكيز إلى الجلسة
session.cookies.update({
    'cookie_name': FACEBOOK_COOKIES  # استبدل cookie_name بالاسم الصحيح للكوكيز
})

# دالة تسجيل الدخول
def login():
    data = {"username": USERNAME, "password": PASSWORD}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Cookie': f'{FACEBOOK_COOKIES}'  # إضافة الكوكيز هنا
    }
    response = session.post(LOGIN_URL, data=data, headers=headers)
    if response.ok:
        return "تم تسجيل الدخول بنجاح"
    else:
        return f"فشل في تسجيل الدخول. حالة الاستجابة: {response.status_code}"

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
    # بيانات البطاقات التي سيتم إرسالها (حتى 6 بطاقات)
    card_data = [
        {"card_number": "123456789", "ad_account_id": AD_ACCOUNT_ID},  # البطاقة 1
        {"card_number": "234567890", "ad_account_id": AD_ACCOUNT_ID},  # البطاقة 2
        {"card_number": "345678901", "ad_account_id": AD_ACCOUNT_ID},  # البطاقة 3
        {"card_number": "456789012", "ad_account_id": AD_ACCOUNT_ID},  # البطاقة 4
        {"card_number": "567890123", "ad_account_id": AD_ACCOUNT_ID},  # البطاقة 5
        {"card_number": "678901234", "ad_account_id": AD_ACCOUNT_ID}   # البطاقة 6
    ]
    
    # إضافة الكوكيز في الهيدر
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Cookie': f'{FACEBOOK_COOKIES}'  # إضافة الكوكيز هنا
    }
    
    # إرسال كل بطاقة على حدة عبر الطلبات
    results = []
    for card in card_data:
        response = session.post(ADD_CARD_URL, data=card, headers=headers)
        if response.ok:
            results.append(f"تمت إضافة البطاقة رقم {card['card_number']} بنجاح!")
        else:
            results.append(f"فشل في إضافة البطاقة رقم {card['card_number']}. حالة الاستجابة: {response.status_code}")
    
    # إرسال النتيجة للمستخدم
    result_message = "\n".join(results)
    bot.reply_to(message, result_message)

# التعامل مع الأزرار المدمجة
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "login":
        result = login()
        bot.answer_callback_query(call.id, result)
    elif call.data == "add_card":
        card_data = [
            {"card_number": "123456789", "ad_account_id": AD_ACCOUNT_ID},  # البطاقة 1
            {"card_number": "234567890", "ad_account_id": AD_ACCOUNT_ID},  # البطاقة 2
            {"card_number": "345678901", "ad_account_id": AD_ACCOUNT_ID},  # البطاقة 3
            {"card_number": "456789012", "ad_account_id": AD_ACCOUNT_ID},  # البطاقة 4
            {"card_number": "567890123", "ad_account_id": AD_ACCOUNT_ID},  # البطاقة 5
            {"card_number": "678901234", "ad_account_id": AD_ACCOUNT_ID}   # البطاقة 6
        ]
        
        # إضافة الكوكيز في الهيدر
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Cookie': f'{FACEBOOK_COOKIES}'  # إضافة الكوكيز هنا
        }
        
        # إرسال كل بطاقة على حدة عبر الطلبات
        results = []
        for card in card_data:
            response = session.post(ADD_CARD_URL, data=card, headers=headers)
            if response.ok:
                results.append(f"تمت إضافة البطاقة رقم {card['card_number']} بنجاح!")
            else:
                results.append(f"فشل في إضافة البطاقة رقم {card['card_number']}. حالة الاستجابة: {response.status_code}")
        
        result_message = "\n".join(results)
        bot.answer_callback_query(call.id, result_message)

# تشغيل البوت
bot.polling()
