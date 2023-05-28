from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.pathUtils import *
import model.venueModel

upMenuStr = "👆 Go to the Previous Menu"

# Buttons of Main Options
def view_button_main(crntPath : str):
    keyboard = [
        [InlineKeyboardButton("Previous Orders", callback_data = addToPath(crntPath, "previous_orders"))],
        [InlineKeyboardButton("Orders in Place", callback_data = addToPath(crntPath, "ods_inplace"))],
        [InlineKeyboardButton("Select Categories to Explore", callback_data = addToPath(crntPath, "vn_ctgs"))],
        [InlineKeyboardButton("Venue Preferences", callback_data = addToPath(crntPath, "venue_preferences"))],
        [InlineKeyboardButton("Learn More", callback_data = addToPath(crntPath, "l_m"))]
        ]
    return InlineKeyboardMarkup(keyboard)

def view_button_previous_orders(crntPath : str):
    keyboard = [
        [InlineKeyboardButton("Order 1", callback_data = addToPath(crntPath, "order_1_id"))],
        [InlineKeyboardButton("Order 2", callback_data = addToPath(crntPath, "order_2_id"))],
        [InlineKeyboardButton("Order 3", callback_data = addToPath(crntPath, "order_3_id"))],
        [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]
        ]
    return InlineKeyboardMarkup(keyboard)

def view_button_venue_preferences(crntPath : str):
    keyboard = [
        [InlineKeyboardButton("Wheelchair Accessibility", callback_data = addToPath(crntPath, "wheelchair_accessibility"))],
        [InlineKeyboardButton("Sign Language", callback_data = addToPath(crntPath, "sign_language"))],
        [InlineKeyboardButton("Blind Friendly Entrance", callback_data = addToPath(crntPath, "blind_friendly"))],
        [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]
        ]
    return InlineKeyboardMarkup(keyboard)


# Buttons of Venues
def view_button_vn_ctgs(crntPath : str):
    keyboard = [
        [InlineKeyboardButton("🍔 Food", callback_data = addToPath(crntPath, "food"))],
        [InlineKeyboardButton("☕️ Coffee", callback_data = addToPath(crntPath, "coffee"))],
        [InlineKeyboardButton("💄 Beauty", callback_data = addToPath(crntPath, "beauty"))],
        [InlineKeyboardButton("⏮ Upcoming Others ⏭", callback_data = "main")],
        [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]
        ]
    return InlineKeyboardMarkup(keyboard)

def view_button_venues_in_category(crntPath : str):
    type = lastPathParam(crntPath)
    keyboard = []
    for venue in model.venueModel.venues:
        keyboard.append( [InlineKeyboardButton(venue["name"], callback_data = addToPath(crntPath, venue["id"]))] )
    keyboard.append( [InlineKeyboardButton(f"Other {type}s", callback_data = "main")] )
    keyboard.append( [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))] )
    return InlineKeyboardMarkup(keyboard)

def view_button_venue_detail(crntPath : str):
    # venue_id = lastPathParam(crntPath)
    keyboard = [
        [InlineKeyboardButton("View the Menu/Services", callback_data = addToPath(crntPath, "view_menu"))],
        [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]
        ]
    return InlineKeyboardMarkup(keyboard)

def view_button_menu_detail(crntPath : str):
    params = splitPathStr(crntPath)
    type = params[-3]
    venue_id = params[-2]
    keyboard = []
    for venue in model.venueModel.venues:
        if venue["id"] == venue_id:
            for item in venue["menu"]:
                keyboard.append( [InlineKeyboardButton(item["name"], callback_data = addToPath(crntPath, item["id"]))] )
    
    keyboard.append( [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))] )
    return InlineKeyboardMarkup(keyboard)

def view_button_item_detail(crntPath : str):
    params = splitPathStr(crntPath)
    type = params[-4]
    venue_id = params[-3]
    keyboard = [
        [InlineKeyboardButton("Order and Pay Now", callback_data = addToPath(crntPath, "order_pay"))],
        [InlineKeyboardButton("Just Order (Pay at the Venue)", callback_data = addToPath(crntPath, "order"))],
        [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]
        ]
    return InlineKeyboardMarkup(keyboard)

def view_button_back(crntPath : str):
    return InlineKeyboardMarkup( [[InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))]] )


def view_button_undeveloped(crntPath : str):
    return InlineKeyboardMarkup( [[InlineKeyboardButton("👆 Undeveloped, Go to the Top Menu", callback_data = "main")]] )
