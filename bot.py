"""educational telegram bot"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    """Method for processing the start command."""
    print('start put')
    user_id = update['message']['chat']['id']
    update.message.reply_text(f'Hello user, your id = {user_id}')


def talk_to_me(update, context):
    """Text message processing method."""
    text = update.message.text
    print(text)
    if text == 'exit':
        print('start exit')
        exit()
    update.message.reply_text(text)


def main():
    """Method for starting the bot."""
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot start')
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
