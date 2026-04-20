import os
import telebot
from flask import Flask
from threading import Thread

# Замените 'YOUR_BOT_TOKEN' на реальный токен вашего бота
BOT_TOKEN = 'YOUR_BOT_TOKEN'

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask('')

# Здесь будет вся логика вашего бота (обработчики команд и т.д.)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я работаю на Koyeb!')

# Этот обработчик нужен, чтобы бот отвечал на текстовые сообщения
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