from telegram import Update
from telegram.ext import ContextTypes

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Thank you for your payment!")