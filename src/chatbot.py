import time
import telepot
from telepot.loop import MessageLoop
import random
from keywords import *
        
def handle(msg):
    # Read information of incoming message.
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    # Iterate over keywords and possible answers.
    for keywords in DATA:
        if content_type == 'text' and any(keyword in msg['text'].lower() for keyword in keywords):
            bot.sendMessage(chat_id, random.choice(DATA[keywords]))

    if content_type == 'text' and msg['text'].lower() == 'selbstzerstörung':
        bot.sendMessage(chat_id, '10')
        bot.sendMessage(chat_id, '9')
        bot.sendMessage(chat_id, '8')
        bot.sendMessage(chat_id, '7')
        bot.sendMessage(chat_id, '6')
        bot.sendMessage(chat_id, '5')
        bot.sendMessage(chat_id, '4')
        bot.sendMessage(chat_id, '3')
        bot.sendMessage(chat_id, '2')
        bot.sendMessage(chat_id, '1')
        bot.sendMessage(chat_id, '0')
        bot.sendMessage(chat_id, '...')
        bot.sendMessage(chat_id, 'Ups.. Das hat wohl leider nicht geklappt.')
        
    if content_type == 'photo' or content_type == 'video':
        bot.sendMessage(chat_id, 'Das ist doch ein Porno!')

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
