import os
import telebot
from flask import Flask
from threading import Thread

# 1. ЗДЕСЬ ВАШ ТОКЕН
BOT_TOKEN = '8737521251:AAGpW6bvG1vZRTx279pjD8KnWqfOvtx4HE0'

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask('')

# Здесь будет вся логика вашего бота
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я работаю на Koyeb!')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Веб-сервер для Koyeb
@app.route('/')
def home():
    return "Бот работает!"

# Запуск бота в отдельном потоке
def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # Запускаем бота в фоновом потоке
    t = Thread(target=run_bot)
    t.start()
    # Запускаем веб-сервер
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8000)))
