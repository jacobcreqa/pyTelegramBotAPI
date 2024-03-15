import os
import telebot

#bot = telebot.TeleBot("7039625967:AAGDIWEqVmTq_ZIkVk52cv8rP2eXRgHHTQQ")
bot = telebot.TeleBot(os.environ["TELEBOT_BOT_TOKEN"])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, ==>:" + os.environ["TELEBOT_BOT_TOKEN"])

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	
bot.infinity_polling()