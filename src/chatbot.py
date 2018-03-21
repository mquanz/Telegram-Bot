import time
import telepot
from telepot.loop import MessageLoop
import random
from keywords import *

def handle(msg):
	# Read information of user writing.
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text' and any(keyword in msg['text'] for keyword in SAUFEN):
        bot.sendMessage(chat_id, random.choice(ANSW_SAUFEN))

    elif content_type == 'text' and any(keyword in msg['text'] for keyword in BIER):
        bot.sendMessage(chat_id, random.choice(ANSW_BIER))

    elif content_type == 'sticker':
        bot.sendMessage(chat_id, random.choice(SMILEYS))

    elif content_type == 'text' and any(keyword in msg['text'] for keyword in VEGAN):
        bot.sendMessage(chat_id, ANSW_VEGAN)


# To get your own token, contact @BotMaster in Telegram.
with open('token.txt') as f:
    token = f.readline()
token = token.strip('\n')

bot = telepot.Bot(token)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
