from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

from view.buttons import view_button_main

from utils.envUtils import ENV

from model.locationsModel import initLocations
import handler.location, handler.payment, handler.button

import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to the 5quare Bot!", reply_markup = view_button_main("main"))

def main() -> None:
    application = Application.builder().token(ENV.TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handler.button.handler))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, handler.payment.handler))
    application.add_handler(MessageHandler(filters.LOCATION, handler.location.handler))
    application.run_polling()

if __name__ == "__main__":
    # initLocations()
    main()
