from telegram.ext import ContextTypes
from .pathUtils import splitPathStr

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
        "milk_allergy": context.chat_data.get("milk_allergy", False),
        "other_allergy": context.chat_data.get("other_allergy", False)
        }