# pip install python-telegram-bot
from telegram.ext import *
import random
import Foodie
token = '5472012676:AAGUprVAPB56WlV3SDyEEW82NFldYcwKFmI'

print('Starting up bot...')


# Lets us use the /start command
def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. What\'s up?')


# Lets us use the /help command
def help_command(update, context):
    update.message.reply_text('Try typing "surprise" or "surprise me" and I will do my best to respond!')


# Lets us use the /custom command
def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_response(text) -> str:
    # Create your own response logic
    length = len(Foodie.food)
    rnd = random.randint(0,length)

    if 'surprise' in text:
        return Foodie.food[rnd]

    if 'surprise me' in text:
        return Foodie.food[rnd]

    return 'I don\'t understand'


def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if '@gcfoodie_bot' in text:
            new_text = text.replace('@gcfoodie_bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    # Reply normal if the message is in private
    update.message.reply_text(response)


# Log errors
def error(update, context):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()