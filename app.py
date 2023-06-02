from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

from routes import choosePath
from view.buttons import view_button_main
from view.descriptions import textForPath

from utils.prefUtils import *
from utils import payments
from utils.envUtils import ENV

from model.locationsModel import initLocations

import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to the 5quare Bot!", reply_markup = view_button_main("main"))

async def buttonHandler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    path = query.data
    if path.endswith("_pref"):
        # This should be before than choosePath.
        await handlePref(path, context=context)
    elif path.endswith("order_pay"):
        await payments.handlePayments(update, context)
        return
    reply_markup = choosePath(path, context)
    await query.answer()
    await query.edit_message_text(text = textForPath(path), parse_mode="HTML", reply_markup = reply_markup)

async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Thank you for your payment!")

def main() -> None:
    application = Application.builder().token(ENV.TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(buttonHandler))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))
    application.run_polling()

if __name__ == "__main__":
    initLocations()
    main()
