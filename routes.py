from telegram import InlineKeyboardMarkup
from telegram.ext import ContextTypes
from view.buttons import *

def choosePath(path : str, context : ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    array = splitPathStr(path)
    print(array)
    if len(array) == 1:
        return view_button_main("main")
    elif len(array) == 2:
        lastHandle = array[-1]
        if lastHandle == "venue_preferences":
            return view_button_venue_preferences(path, context)
        else:
            return returnFunc(path, callbacks[lastHandle])
    elif len(array) == 3:
        # List Venues in Selected Category
        if array[1] == "vn_ctgs":
            return view_button_venues_in_category(path)
        elif array[-2] == "venue_preferences":
            # Remove last item, because it has been processed before.
            path = combinePaths(splitPathStr(path)[:-1])
            return view_button_venue_preferences(path, context)
    elif len(array) == 4:
        # Venue Details
        if array[1] == "vn_ctgs":
            return view_button_venue_detail(path)
    elif len(array) == 5:
        # Lists Menu
        if array[1] == "vn_ctgs":
            return view_button_menu_detail(path)
    elif len(array) == 6:
        # Menu Item Details
        if array[1] == "vn_ctgs":
            return view_button_item_detail(path)
    else:
        return view_button_main("main")

def returnFunc(s : str, callback):
    return callback(s)


callbacks = {
    "main": view_button_main,
    "previous_orders": view_button_previous_orders,
    "venue_preferences": view_button_venue_preferences,
    "ods_inplace": view_button_undeveloped,
    "l_m": view_button_back,
    "vn_ctgs": view_button_vn_ctgs
    }
