from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

from utils import payments
from utils.prefUtils import setPref, getPrefs, warningTextForUser

from model.flowModel import markups
import model.venueModel

upMenuStr = "👆 Go to "

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    replyType = "callback"
    
    # We got the location of user
    # TODO: Add a sorting according to the distance to the user.
    if hasattr(update.message, "location"):
        location = update.message.location
        key = "categories"
        replyType = "location"
    else:
        key = query.data
    
    keyParam = key.split("&")
    key = keyParam[0]
    param = keyParam[1] if len(keyParam) >= 2 else ""
    decorator = keyParam[2] if len(keyParam) > 2 else ""
    text = markups[key]["text"]
    
    children = markups[key]["children"] if markups[key].__contains__("children") else []
    keyboard = []
    
    # Set Parameter in Chat Data
    if param != "" and decorator == "+":
        prefName = param
        prefVal = getPrefs(context)[prefName]        
        prefVal = (not prefVal)
        await setPref(prefName=prefName, value=prefVal, context=context)

    
    elif key == "food" or key == "coffee" or key ==  "beauty":
        # Insert venue=id keys as children
        children = list(map(lambda x: "venue=" + str(x["id"]), model.venueModel.venues))
        children.append("<categories")
    
    elif key.startswith("item"):
        itemId = key.split("=")[1]
        text += warningTextForUser(itemId=itemId, context=context)
    
    elif key == "_pay":
        print("here")
    
    """
    ITERATE OVER CHILDS
    """
    for child in children:
                        
        # Retrieve Go Back Items
        if child.startswith("<"):
            child = child[1:]
            keyboard.append( [InlineKeyboardButton( upMenuStr + markups[child]["name"], callback_data = child )] )
        
        # Retrieve Items with ID
        elif child.startswith("_"):
            keyboard.append( [InlineKeyboardButton( "Order and Pay", callback_data = child )] )
                    
        # Retrieve Standards Items with keys
        else:

            if key == "venue_preferences" or key == "food_preferences":
                keyboard.append( basePrefOption(child=child, context=context, key=key) )
            
            elif key == "pay":
                """
                We cannot use Square's payment api with Telegram's native payment module.
                Also we didn't wanted to get credit card details as a text message in Telegram.
                And other payment providers such as Stripe generally is not working in Sandbox mode.
                There is a problem between Telegram and Stripe.
                Even there is a problem, Payment feature of Telegram and Whatsapp provides secure,
                reliable and easy implementations.
                """
                orderId = param
                keyboard = [[ InlineKeyboardButton( "Placing your order", callback_data = "<main") ]]
  
            else:
                keyboard.append( [InlineKeyboardButton( markups[child]["name"], callback_data = child )] )
    
    
    if replyType == "location":
        await update.message.reply_text(text=text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await query.answer()
        await query.edit_message_text( text = text, parse_mode="HTML", reply_markup = InlineKeyboardMarkup(keyboard) )

    

def basePrefOption(child, context, key) -> list:
    path = child.split("&")
    prefName = path[1]
    prefVal = getPrefs(context)[prefName]
    buttonTitle = markups[prefName]["name"] + (" ✅" if prefVal else "")
    buttonVal = key + "&" + prefName + "&" + "+"
    return [InlineKeyboardButton( buttonTitle, callback_data = buttonVal )]
    