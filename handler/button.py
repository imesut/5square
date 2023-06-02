from telegram import Update
from telegram.ext import ContextTypes

from routes import choosePath

from utils import payments
from utils.prefUtils import *

from view.descriptions import textForPath


async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
