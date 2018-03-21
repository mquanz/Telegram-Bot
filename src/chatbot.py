import time
import telepot
from telepot.loop import MessageLoop

def handle(msg):
	# Read information of user writing.
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text' and msg['text'].find('Bier') != -1 or content_type == 'text' and msg['text'].find('bier') != -1:
        bot.sendMessage(chat_id, 'Bier? Ja klar, ich will saufen!')

    elif content_type == 'sticker':
        bot.sendMessage(chat_id, 'Smileys sind scheiße!')

#To get your own token, contact @BotMaster in Telegram.
with open('token.txt') as f:
    token = f.readline()
token = token.strip('\n')

bot = telepot.Bot(token)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

#Keep the program running.
while 1:
    time.sleep(10)
