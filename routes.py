from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
import logging

pathSplitChar = ">>>"
upMenuStr = "👆 Go to the Previous Menu"

def choosePath(path : str) -> InlineKeyboardMarkup:
    array = splitPathStr(path)
    if len(array) == 1:
        return route_main("main")
    elif len(array) == 2:
        lastHandle = array[-1]
        return returnFunc(path, callbacks[lastHandle])
    else:
        return route_main("main")

def returnFunc(s : str, callback):
    return callback(s)



# Routes of Main Options
def route_main(crntPath : str):
    keyboard = [
        [InlineKeyboardButton("Previous Orders", callback_data = addToPath(crntPath, "previous_orders"))],
        [InlineKeyboardButton("Orders in Place", callback_data = addToPath(crntPath, "orders_in_place") )],
        [InlineKeyboardButton("Venue Preferences", callback_data = addToPath(crntPath, "venue_preferences"))],
        [InlineKeyboardButton("Learn More", callback_data = addToPath(crntPath, "learn_more"))]
        ]
    return InlineKeyboardMarkup(keyboard)

def route_previous_orders(crntPath : str):
    keyboard = [
        [InlineKeyboardButton("Order 1", callback_data = addToPath(crntPath, "order_1_id"))],
        [InlineKeyboardButton("Order 2", callback_data = addToPath(crntPath, "order_2_id") )],
        [InlineKeyboardButton("Order 2", callback_data = prvPath(crntPath) )]
        ]
    return InlineKeyboardMarkup(keyboard)

def route_venue_preferences(crntPath : str):
    keyboard = [
        [InlineKeyboardButton("Wheelchair Accessibility", callback_data = addToPath(crntPath, "wheelchair_accessibility"))],
        [InlineKeyboardButton("Sign Language", callback_data = addToPath(crntPath, "sign_language"))],
        [InlineKeyboardButton("Blind Friendly Entrance", callback_data = addToPath(crntPath, "blind_friendly"))],
        [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]
        ]
    return InlineKeyboardMarkup(keyboard)

def route_undeveloped(crntPath : str):
    keyboard = [[InlineKeyboardButton("👆 Undeveloped", callback_data = "main")]]
    return InlineKeyboardMarkup(keyboard)

callbacks = {
    "main": route_main,
    "previous_orders": route_previous_orders,
    "venue_preferences": route_venue_preferences,
    "orders_in_place": route_undeveloped,
    "learn_more": route_undeveloped
    }

# Path Utils
def combinePaths(pathArray : list) -> str:
    return pathSplitChar.join(pathArray)

def splitPathStr(pathString : str) -> list:
    return pathString.split(pathSplitChar)

def addToPath(str1 : str, str2 : str) -> str:
    return str1 + pathSplitChar + str2

def prvPath(crntPath : str) -> str:
    return combinePaths(splitPathStr(crntPath)[:-1])