import time
import telepot
from telepot.loop import MessageLoop
import random

# Keywords:
SAUFEN = ['SAUFEN', 'saufen', 'Saufen', 'BALLERN', 'Ballern', 'ballern', 'TRINKEN', 'trinken', 'Trinken']
BIER = ['Bier', 'bier', 'BIER']

# Answers:
ANSW_SAUFEN = ['JAMAN, richtig was installieren!', 'Ich will BALLERN!', 'Morgens, mittags, abends ich will saufen!']
ANSW_BIER = ['Hab ich da eben Bier gehört?', 'Ja geil, schön rein in den Schlund!', 'Bier ist eben ein Grundnahrungsmittel.']
SMILEYS = ['Hübscher Smiley..', 'Ich hasse diese Sticker!', 'Hört doch endlich mal auf mit diesen Stickern!!!11!!']

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
