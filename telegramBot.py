import sys
import time
import random
import datetime
import telepot
import picamera

# name and dimentsions of snapshot image
IMG_WIDTH = 800
IMG_HEIGHT = 600
#image DIR
IMAGE_DIR = "/home/pi/"
#Image name
IMG = "foto.jpg"
def handle(msg):
	chat_id=msg['chat']['id']
	command = msg['text']
	
	print 'Got command: %s' % command

	if command == '/roll':
		bot.sendMessage(chat_id, random.randint(1,6))
	elif command == '/time':
		bot.sendMessage(chat_id, str(datetime.datetime.now()))
	elif command == '/photo':
		with picamera.PiCamera() as camera:
			camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
			camera.start_preview()
			time.sleep(1)
			camera.capture(IMAGE_DIR + IMG)
		bot.sendPhoto(chat_id, open(IMAGE_DIR + IMG, 'rb'))

bot = telepot.Bot('177155552:AAGIqQ54q_mA-2d3AHClccTcDh8hsdhsNuM')
bot.notifyOnMessage(handle)
print 'I am Listening ... '

while 1:
	time.sleep(10)

