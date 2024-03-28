import telebot;
import random as ran
from telebot import types
bot = telebot.TeleBot('6934571077:AAFtnH7b27PTtaTIzIqml04ku8s6Ltuu8Jw');

game_in_progress = {}

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "Чаво")

@bot.message_handler(content_types=['text'])
def start(message):
	keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	button1 = types.KeyboardButton('/гра')
	button2 = types.KeyboardButton('/Сігма')
	button3 = types.KeyboardButton('/ХУЙ')
	keyboard.add(button1, button2, button3)

	print(f'{message.from_user.username} {message.from_user.first_name}')

	if message.text == "/Сігма":
		bot.send_message(message.chat.id, "https://www.tiktok.com/@markovv_tt/video/7196927034457672965?is_from_webapp=1&sender_device=pc")
	elif message.text.startswith("/пасхалко") or message.text.startswith("/1488") or message.text.startswith("/Пасхалко"):
		bot.send_message(message.chat.id, "што?🤣🤣🤣посхолко😳😳🤪кто заминетил🤣🤣🤣включаем вінтілітори🤣🤣🤣🤪🤪💪💪")
	elif message.text.startswith("/r34"):
		print('Ruler')
	elif message.text == "/help":
		bot.send_message(message.chat.id, text='Підсказки', reply_markup=keyboard)
	elif message.text == "/гра":
		if game_in_progress.get(message.chat.id):
			bot.send_message(message.chat.id, "Гра вже йде!")
		else:
			game_in_progress[message.chat.id] = True
			keyboard = types.InlineKeyboardMarkup()
			key_1= types.InlineKeyboardButton(text='камінь', callback_data='1')
			keyboard.add(key_1)
			key_2 = types.InlineKeyboardButton(text='папір', callback_data='2')
			keyboard.add(key_2)
			key_3= types.InlineKeyboardButton(text='ножиці', callback_data='3')
			keyboard.add(key_3)
			bot.send_message(message.chat.id, text='Камін, ножиці, папір', reply_markup=keyboard)
	elif message.text == "/ХУЙ":
		bot.send_message(message.chat.id, "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬛⬛⬜\n⬜⬛⬜⬛⬜⬜⬜\n⬜⬛⬜⬛⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜⬛⬜\n⬜⬜⬜⬛⬜⬛⬜\n⬜⬛⬛⬛⬜⬜⬜")
	else:
		bot.send_message(message.chat.id, "Чо?")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	if not game_in_progress.get(call.message.chat.id):
		return

	s=ran.randint(1, 3)
	if call.data == "1":
		if s==1:
			bot.send_message(call.message.chat.id, '-Камінь')
			bot.send_message(call.message.chat.id, 'Нічия')
		elif s==2:
			bot.send_message(call.message.chat.id, '-Папір')
			bot.send_message(call.message.chat.id, 'Поразка')
		elif s==3:
			bot.send_message(call.message.chat.id, '-Ножиці')
			bot.send_message(call.message.chat.id, 'Перемога')
	elif call.data == "2":
		if s==1:
			bot.send_message(call.message.chat.id, '-Камінь')
			bot.send_message(call.message.chat.id, 'Перемога')
		elif s==2:
			bot.send_message(call.message.chat.id, '-Папір')
			bot.send_message(call.message.chat.id, 'Нічия')
		elif s==3:
			bot.send_message(call.message.chat.id, '-Ножиці')
			bot.send_message(call.message.chat.id, 'Поразка')
	elif call.data == "3":
		if s==1:
			bot.send_message(call.message.chat.id, '-Камінь')
			bot.send_message(call.message.chat.id, 'Поразка')
		elif s==2:
			bot.send_message(call.message.chat.id, '-Папір')
			bot.send_message(call.message.chat.id, 'Перемога')
		elif s==3:
			bot.send_message(call.message.chat.id, '-Ножиці')
			bot.send_message(call.message.chat.id, 'Нічия')

	game_in_progress[call.message.chat.id] = False

bot.polling(none_stop=True, interval=0)