from telegram.ext import ContextTypes
from .pathUtils import splitPathStr

# TODO persistent storage ?

async def handlePref(path : str, context : ContextTypes.DEFAULT_TYPE):
    print(path, context)
    if path.endswith("_pref"):
        array = splitPathStr(pathString = path)
        prefKeys = array[-1]
        prefKeys = prefKeys.split("_")
        pref = prefKeys[0] # whl / sign / blind
        state = prefKeys[1] # enbl / disbl
        if state == "enbl":
            context.chat_data[pref] = True
        else:
            context.chat_data[pref] = False
    
def getPrefs(context : ContextTypes.DEFAULT_TYPE):
    return {
        "whl": context.chat_data.get("whl", False),
        "sign": context.chat_data.get("sign", False),
        "blind": context.chat_data.get("blind", False)
        }