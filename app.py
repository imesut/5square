from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

from model.squareModels.locationsModel import initLocations
from model.flowModel import markups, insertItemsToFlow
import buttonHandler

from utils.envUtils import ENV
import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    text = markups["main"]["text"]
    children = markups["main"]["children"]
    keyboard = []
    
    for child in children:
        keyboard.append( [InlineKeyboardButton( markups[child]["name"], callback_data = child )] )
    
    await update.message.reply_text(text, parse_mode="HTML", reply_markup = InlineKeyboardMarkup(keyboard))

def main() -> None:
    application = Application.builder().token(ENV.TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(buttonHandler.handler))
    # application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, handler.payment.handler))
    application.add_handler(MessageHandler(filters.LOCATION, buttonHandler.handler))
    application.run_polling()

if __name__ == "__main__":
    initLocations()
    insertItemsToFlow()
    main()
