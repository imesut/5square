from telegram.ext import ContextTypes
from .pathUtils import splitPathStr
from model.venueModel import getVenue, getItemWoVenue


# TODO persistent storage ?

# async def handlePref(path : str, context : ContextTypes.DEFAULT_TYPE):
#     print(path, context)
#     if path.endswith("_pref"):
#         array = splitPathStr(pathString = path)
#         prefKeys = array[-1]
#         prefKeys = prefKeys.split("_")
#         pref = prefKeys[0] # whl / sign / blind
#         state = prefKeys[1] # enbl / disbl
#         if state == "enbl":
#             context.chat_data[pref] = True
#         else:
#             context.chat_data[pref] = False

async def setPref(prefName : str, value, context : ContextTypes.DEFAULT_TYPE):
    context.chat_data[prefName] = value

def getPrefs(context : ContextTypes.DEFAULT_TYPE):
    return {
        "whl": context.chat_data.get("whl", False),
        "sign": context.chat_data.get("sign", False),
        "blind": context.chat_data.get("blind", False),
        "vegetarian": context.chat_data.get("vegetarian", False),
        "gluten_allergy": context.chat_data.get("gluten_allergy", False),
        "lactose_allergy": context.chat_data.get("lactose_allergy", False),
        "other_allergy": context.chat_data.get("other_allergy", False)
        }


def warningTextForUser(itemId : str, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = "\n\n"
    userPrefs = getPrefs(context=context)
    itemProps = getItemWoVenue(itemId)
    
    print("debug", userPrefs, itemProps)
    
    if userPrefs["vegetarian"]:
        if userPrefs["vegetarian"] != itemProps["vegetarian"]:
            text += "❌ Not suitable with your <i>Vegetarian</i> preference. \n"
    
    if userPrefs["gluten_allergy"]:
        if userPrefs["gluten_allergy"] != itemProps["gluten_free"]:
            text += "❌ Contains <i>Gluten</i>\n"
        else:
            text += "Safe to consume, <b>Gluten-free</b> ✅\n"
        
    if userPrefs["lactose_allergy"]:
        if userPrefs["lactose_allergy"] != itemProps["lactose_free"]:
            text += "❌ Contains <i>Lactose</i>\n"
        else:
            text += "Safe to consume, <b>Lactose-free</b> ✅\n"
        
    text += "\n"
    return text
