import os, time
import telebot
import sqlite3
from telebot import *
bot = telebot.TeleBot('964957577:AAHQlnTDLdyLxDsrnsSE8M0HcxRwMup6YDk')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
keyboard1.row('Отправить сообщение')
@bot.message_handler(commands=['start'])
def start_message(message):
    msg = "x"
    bot.send_message(message.chat.id, msg, reply_markup=keyboard1)
    user = message.chat.id
    f = open("ids.txt", "a")
    user2 = str(user)
    userj = user2 + "\n"
    f.write(userj)
@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text.lower() == 'отправить сообщение':
		def mess(message):
			print(message.chat.id)
			try :
				userm = message.text
				print(userm)
				print(message.chat.username)
				print(message.chat.id)			
				print(message.chat.first_name)
				print(message.chat.last_name)
				print("-------")
			except:
				pass
			f = open("ids.txt", "r")
			for line in f:
				try:
					bot.send_message(line, userm)
				except:
					try:
						bot.send_photo(line, photo=message.content)
					except:
						pass
		sent = bot.send_message(message.chat.id, "Введи сообщение")
		bot.register_next_step_handler(sent, mess)
bot.polling(none_stop=True)
