import os
from telegram.ext import CommandHandler

TOKEN = "656898492:AAEb-md0fuE3pkAu3J_Hxqljqci2jojtA-Q"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
# add handlers
def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Talk to me")

def help(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Say hello to your overlord")

start_handler = CommandHandler('start', start)
dispatcher.add_handler (start_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler (help_handler)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://<appname>.herokuapp.com/" + TOKEN)
updater.idle()