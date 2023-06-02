from telegram import Update
from telegram.ext import ContextTypes
from view.buttons import view_button_vn_ctgs

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message.location)
    await update.message.reply_text("Hi", reply_markup = view_button_vn_ctgs("main>>vn_ctgs"))

