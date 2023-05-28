from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
from utils.pathutils import *

upMenuStr = "👆 Go to the Previous Menu"

def choosePath(path : str) -> InlineKeyboardMarkup:
    array = splitPathStr(path)
    print(array)
    if len(array) == 1:
        return route_main("main")
    elif len(array) == 2:
        lastHandle = array[-1]
        return returnFunc(path, callbacks[lastHandle])
    elif len(array) == 3:
        # List Venues in Selected Category
        if array[1] == "vn_ctgs":
            return route_venues_in_category(path)
    elif len(array) == 4:
        # Venue Details
        if array[1] == "vn_ctgs":
            return route_venue_detail(path)
    elif len(array) == 5:
        # Lists Menu
        if array[1] == "vn_ctgs":
            return route_menu_detail(path)
    elif len(array) == 6:
        # Menu Item Details
        if array[1] == "vn_ctgs":
            return route_item_detail(path)
    else:
        return route_main("main")

def returnFunc(s : str, callback):
    return callback(s)



# Routes of Main Options
def route_main(crntPath : str):
    keyboard = [
        [InlineKeyboardButton("Previous Orders", callback_data = addToPath(crntPath, "previous_orders"))],
        [InlineKeyboardButton("Orders in Place", callback_data = addToPath(crntPath, "ods_inplace"))],
        [InlineKeyboardButton("Select Categories to Explore", callback_data = addToPath(crntPath, "vn_ctgs"))],
        [InlineKeyboardButton("Venue Preferences", callback_data = addToPath(crntPath, "venue_preferences"))],
        [InlineKeyboardButton("Learn More", callback_data = addToPath(crntPath, "l_m"))]
        ]
    return InlineKeyboardMarkup(keyboard)

def route_previous_orders(crntPath : str):
    keyboard = [
        [InlineKeyboardButton("Order 1", callback_data = addToPath(crntPath, "order_1_id"))],
        [InlineKeyboardButton("Order 2", callback_data = addToPath(crntPath, "order_2_id"))],
        [InlineKeyboardButton("Order 3", callback_data = addToPath(crntPath, "order_3_id"))],
        [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]
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


# Routes of Venues
def route_vn_ctgs(crntPath : str):
    keyboard = [
        [InlineKeyboardButton("🍔 Food", callback_data = addToPath(crntPath, "food"))],
        [InlineKeyboardButton("☕️ Coffee", callback_data = addToPath(crntPath, "coffee"))],
        [InlineKeyboardButton("💄 Beauty", callback_data = addToPath(crntPath, "beauty"))],
        [InlineKeyboardButton("⏮ Upcoming Others ⏭", callback_data = "main")],
        [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]
        ]
    return InlineKeyboardMarkup(keyboard)

def route_venues_in_category(crntPath : str):
    type = lastPathParam(crntPath)
    keyboard = [
        [InlineKeyboardButton(f"{type} Place 1", callback_data = addToPath(crntPath, "vn_id_1"))],
        [InlineKeyboardButton(f"{type} Place 2", callback_data = addToPath(crntPath, "vn_id_2"))],
        [InlineKeyboardButton(f"{type} Place 3", callback_data = addToPath(crntPath, "vn_id_3"))],
        [InlineKeyboardButton(f"Other {type}s", callback_data = "main")],
        [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]
        ]
    return InlineKeyboardMarkup(keyboard)

def route_venue_detail(crntPath : str):
    # venue_id = lastPathParam(crntPath)
    keyboard = [
        [InlineKeyboardButton("Venue Details", callback_data = addToPath(crntPath, "venue_details_detail"))], #TODO: Add details to this screen.
        [InlineKeyboardButton("View the Menu/Services", callback_data = addToPath(crntPath, "view_menu"))],
        [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]
        ]
    return InlineKeyboardMarkup(keyboard)

def route_menu_detail(crntPath : str):
    params = splitPathStr(crntPath)
    type = params[-3]
    venue_id = params[-2]
    keyboard = [
        [InlineKeyboardButton(f"{type} Item 1", callback_data = addToPath(crntPath, "mn_id_1"))],
        [InlineKeyboardButton(f"{type} Item 2", callback_data = addToPath(crntPath, "mn_id_2"))],
        [InlineKeyboardButton(f"{type} Item 3", callback_data = addToPath(crntPath, "mn_id_3"))],
        [InlineKeyboardButton(f"{type} Item 4", callback_data = addToPath(crntPath, "mn_id_4"))],
        [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]
        ]
    return InlineKeyboardMarkup(keyboard)

def route_item_detail(crntPath : str):
    params = splitPathStr(crntPath)
    type = params[-4]
    venue_id = params[-3]
    keyboard = [
        [InlineKeyboardButton("View in 3D", callback_data = addToPath(crntPath, "3d"))],
        [InlineKeyboardButton("Order and Pay Now", callback_data = addToPath(crntPath, "order_pay"))],
        [InlineKeyboardButton("Just Order (Pay at the Venue)", callback_data = addToPath(crntPath, "order"))],
        [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]
        ]
    return InlineKeyboardMarkup(keyboard)


def route_undeveloped(crntPath : str):
    return InlineKeyboardMarkup( [[InlineKeyboardButton("👆 Undeveloped, Go to the Top Menu", callback_data = "main")]] )

callbacks = {
    "main": route_main,
    "previous_orders": route_previous_orders,
    "venue_preferences": route_venue_preferences,
    "ods_inplace": route_undeveloped,
    "l_m": route_undeveloped,
    "vn_ctgs": route_vn_ctgs
    }
