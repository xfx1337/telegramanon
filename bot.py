from forex-python import *
import os, time
import telebot
import sqlite3
from telebot import *
from forex_python.converter import CurrencyRates
c = CurrencyRates()
bot = telebot.TeleBot('964957577:AAHQlnTDLdyLxDsrnsSE8M0HcxRwMup6YDk')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
keyboard1.row('Отправить сообщение')
@bot.message_handler(commands=['start'])
def start_message(message):
    msg = "Привет!"
    bot.send_message(message.chat.id, msg, reply_markup=keyboard1)
    user = message.chat.id
    f = open("ids.txt", "a")
    user2 = str(user)
    userj = user2 + "\n"
    f.write(userj)
@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text.lower() == 'отправить сообщение':
		f = open("black.txt")
		for line in f:
			userstr = str(message.chat.id)
			if userstr in line.strip('\n'):
				bot.send_message(message.chat.id, "Вы получили бан, если вы не согласны напишите в лс поддержке")
				return
			else:
				pass
		try:
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
						bot.send_message(line, message.photo)
					except:
						pass
			f = open("ids.txt", "r")
			for line in f:
				try:
					bot.send_message(line, "Пользователь пишет")
				except:
					pass
			sent = bot.send_message(message.chat.id, "Введи сообщение")
			bot.register_next_step_handler(sent, mess)
		except:
			pass
	if message.text.lower("курс валют"):
		rub_dol = c.get_rate('USD', "RUB")
		bot.send_message(message.chat.id, rub_dol)
bot.polling(none_stop=True)
