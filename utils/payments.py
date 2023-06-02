from telegram import Update, LabeledPrice
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

from .pathUtils import splitPathStr
from utils.envUtils import ENV
from model.venueModel import *

import time

async def handlePayments(update : Update, context : ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    path = query.data
    array = splitPathStr(path)
    venue_id = array[-4]
    item_id = array[-2]
    
    venue = getVenue(venue_id)
    item = getItem(venue=venue, item_id=item_id)
            
    await context.bot.send_invoice(chat_id=update.callback_query.message.chat_id,
                                   title=item["name"],
                                   description="Your order from " + venue["name"] + " paid over " + ENV.APPNAME,
                                   payload="app:" + ENV.APPNAME + "-user-fullname:" + update.callback_query.from_user.full_name + "-timestamp:" + str(int(time.time())),
                                   provider_token=ENV.PAYMENT_PROVIDER_TOKEN,
                                   currency=item["currency"],
                                   prices=[LabeledPrice(label=item["name"], amount=int(item["price"] * 100))]
                                   )
