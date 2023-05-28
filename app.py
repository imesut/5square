from dotenv import load_dotenv
import os

from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
import logging

load_dotenv()
token = os.environ["token"]

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    print(user)
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

def keyboardMarkup(id : int):
    keyboard = [
        [InlineKeyboardButton("Option " + str(id), callback_data = str(id))],
        [InlineKeyboardButton("Option " + str(id*2), callback_data = str(id*2))],
        [InlineKeyboardButton("Option " + str(id*3), callback_data = str(id*3))],
        [InlineKeyboardButton("Option " + str(id*4), callback_data = str(id*4))],
        [InlineKeyboardButton("Option " + str(id*5), callback_data = str(id*5))]


        
        ]
    return InlineKeyboardMarkup(keyboard)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Please choose:", reply_markup = keyboardMarkup(1))

async def buttonHandler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    data = int(query.data)
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    
    await query.edit_message_text(text = str(data), reply_markup = keyboardMarkup(data + 1))
    #await query.edit_message_text(text=f"Selected option: {data}")

async def learn_more(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("button", button))
    application.add_handler(CallbackQueryHandler(buttonHandler))

    application.add_handler(CommandHandler("learn_more", learn_more))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()

if __name__ == "__main__":
    main()
