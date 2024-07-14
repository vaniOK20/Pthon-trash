import telebot
import threading
import time

CHANNEL_ID = -1002140512024

bot = telebot.TeleBot('6721623038:AAHjszLNE_FYuiUcpa-mqILtM_s27K_JIRI')
images = {}
videos = {}
target_time = ''
caption = ''

def send():
	while True:
		current_time = f'{time.localtime()[3]}:{time.localtime()[4]}'
		if target_time == current_time and (images or videos):
			for group in images:
				if images[group]:
					media_group = [telebot.types.InputMediaPhoto(img) for img in images[group]]
					bot.send_media_group(CHANNEL_ID, media_group)
					images[group].clear()
			for group in videos:
				if videos[group]:
					for vid in videos[group]:
						bot.send_video(CHANNEL_ID, vid)
					videos[group].clear()

@bot.message_handler(content_types=['text'])
def handle_text(message):
	global target_time
	if message.from_user.username == 'van20fgh':
		if message.text == 'time':
			bot.send_message(message.chat.id, f'{time.localtime()[3]}:{time.localtime()[4]}')
		elif message.text.startswith('settime'):
			if len(message.text) > 8:
				target_time = message.text[8:]
				bot.send_message(message.chat.id, f'Time set to {target_time}')

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
	global caption
	if message.from_user.username == 'van20fgh':
		if message.caption: caption = message.caption
		if caption not in images: images[caption] = []
		images[caption].append(message.photo[-1].file_id)
		bot.reply_to(message, 'Photo saved')

@bot.message_handler(content_types=['video'])
def handle_video(message):
	global caption
	if message.from_user.username == 'van20fgh':
		if message.caption: caption = message.caption
		if caption not in videos: videos[caption] = []
		videos[caption].append(message.video.file_id)
		bot.reply_to(message, 'Video saved')

threading.Thread(target=send).start()

bot.polling(none_stop=True, timeout=20, long_polling_timeout=20)
