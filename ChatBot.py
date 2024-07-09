import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your chatbot. How can I help you?')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's API token
    updater = Updater("7213765768:AAEBHdQqI2NAcH7WSNm3MUGUOcJp3JPW3U4")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
