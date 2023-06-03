from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

from routes import choosePath

from utils import payments
from utils.prefUtils import setPref, getPrefs, warningTextForUser

from view.buttons import markups
from model.venueModel import getVenue, getItemWoVenue

upMenuStr = "👆 Go to "

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    key = query.data
    print(key)
    keyParam = key.split("&")
    print("keyParam", keyParam)
    key = keyParam[0]
    param = keyParam[1] if len(keyParam) >= 2 else ""
    decorator = keyParam[2] if len(keyParam) > 2 else ""
    print("key", key)
    text = markups[key]["text"]
    
    children = markups[key]["children"]
    keyboard = []
    
    # Set Parameter in Chat Data
    if param != "" and decorator == "+":
        prefName = param
        prefVal = getPrefs(context)[prefName]
        
        print(prefName, prefVal)
        
        prefVal = (not prefVal)
        await setPref(prefName=prefName, value=prefVal, context=context)
    
    elif key.startswith("item"):
        itemId = key.split("=")[1]
        print("itemId", itemId)
        text += warningTextForUser(itemId=itemId, context=context)
    
            
    for child in children:
                
        # Retrieve Go Back Items
        if child.startswith("<"):
            child = child[1:]
            keyboard.append( [InlineKeyboardButton( upMenuStr + markups[child]["name"], callback_data = child )] )
        
        # Retrieve Items with ID
        elif child.startswith("_"):
            keyboard.append( [InlineKeyboardButton( "Order and Pay", callback_data = child )] )
                    
        # Retrieve Ordinary Items
        else:
            print("heree", key, text)

            if key == "venue_preferences" or key == "food_preferences":
                keyboard.append( basePrefOption(child=child, context=context, key=key) )
            
            elif key == "pay":
                orderId = param
                keyboard.append( [InlineKeyboardButton( "Placing your order Press to return home", callback_data = "main" )] )
  
            else:
                keyboard.append( [InlineKeyboardButton( markups[child]["name"], callback_data = child )] )
    
    await query.answer()
    await query.edit_message_text( text = text, parse_mode="HTML", reply_markup = InlineKeyboardMarkup(keyboard) )


def basePrefOption(child, context, key) -> list:
    path = child.split("&")
    prefName = path[1]
    prefVal = getPrefs(context)[prefName]
    buttonTitle = markups[prefName]["name"] + (" ✅" if prefVal else "")
    buttonVal = key + "&" + prefName + "&" + "+"
    return [InlineKeyboardButton( buttonTitle, callback_data = buttonVal )]
    