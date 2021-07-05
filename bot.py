from telegram import *
from telegram.ext import *

bot = Bot("1804803062:AAEtGz4iN-_7VXqHSgR6jwzE_dHk4qzrSuo")
#print(bot.get_me())
updater = Updater("1804803062:AAEtGz4iN-_7VXqHSgR6jwzE_dHk4qzrSuo",use_context=True)

def testfunction(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="tutorial link :LOL",
        )
        
dispatcher = updater.dispatcher
start_value = CommandHandler('motion',testfunction)
dispatcher.add_handler(start_value)

def testfunction2(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hellow g",
        )
        
dispatcher = updater.dispatcher
start_value1 = CommandHandler('motion4',testfunction2)
dispatcher.add_handler(start_value1)

updater.start_polling()
