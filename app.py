from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
from routes import choosePath, route_main
import logging

load_dotenv()
token = os.environ["token"]

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Please choose:", reply_markup = route_main("main"))

async def buttonHandler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    path = query.data
    reply_markup = choosePath(path)
    await query.answer()
    await query.edit_message_text(text = path, reply_markup = reply_markup)

def main() -> None:
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(buttonHandler))
    application.run_polling()

if __name__ == "__main__":
    main()
