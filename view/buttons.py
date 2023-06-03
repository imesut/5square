from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.pathUtils import *
import model.venueModel

import utils.prefUtils
import random

upMenuStr = "👆 Go to the Previous Menu"

markups = {
    "main": {
        "text": "<b>Welcome to AllSquare.</b>\nYou can shop at places that provide payment infrastructure and offer you a personalized experience with the Square platform.",
        "name": "Main Menu",
        "children": [ "categories", "venue_preferences", "food_preferences", "learn_more" ]
    },
    "categories": {
        "text": "<b>Closest Places to You.</b>",
        "name": "Categories",
        "children": [ "food", "coffee", "beauty", "upcoming", "<main" ]
    },
    "food": {
        "text": "<b>🍔 Food</b>",
        "name": "🍔 Food",
        "children": [ "venue=1003", "<categories" ]
    },
    "coffee": {
        "text": "<b>☕️ Coffee</b>",
        "name": "☕️ Coffee",
        "children": [ "venue=1003", "<categories" ]
    },
    "beauty": {
        "text": "<b>💄 Beauty</b>",
        "name": "💄 Beauty",
        "children": [ "venue=1003", "<categories" ]
    },
    "upcoming": {
        "text": "<b>⏮ Upcoming Others ⏭</b>",
        "name": "⏮ Upcoming Others ⏭",
        "children": [ "<categories" ]
    },
    # TBC
    "venue_preferences": {
        "text": "<b>Venue Preferences</b>",
        "name": "Venue Preferences",
        "children": [ "venue_preferences&whl", "venue_preferences&sign", "venue_preferences&blind", "<main" ]
    },
    "food_preferences": {
        "text": "<b>Food Preferences</b>",
        "name": "Food Preferences",
        "children": [ "food_preferences&vegetarian", "food_preferences&gluten_allergy", "food_preferences&milk_allergy", "food_preferences&other_allergy", "<main" ]
    },
    "learn_more": {
        "text": "<b>Learn More</b>",
        "name": "Learn More",
        "children": [ "<main" ]
    },
    "whl": { "name": "Wheelchair Accessibility" },
    "sign": { "name": "Sign Language Accessibility" },
    "blind": { "name": "Blind Friendly Accessibility" },
    "_pay": { "text": "Payment in Progress" },
    "vegetarian": { "name": "Prefer Vegetarian options" },
    "gluten_allergy": { "name": "Choose Gluten-free options" },
    "milk_allergy": { "name": "Choose milk-free options" },
    "other_allergy": { "name": "I have another allergy" }
}


for venue in model.venueModel.venues:
    venueKey = "venue=" + venue["id"]
    menuArray = []
    
    for item in venue["menu"]:
        itemKey = "item=" + item["id"]
        menuArray.append( itemKey )
        
        itemDescription = f"<b> { venue['name'].upper() } </b> \n"
        if item["image"] != "":
            itemDescription += f"<a href='{ item['image'] }'>·</a> \n"
        if item["3DModel"] != "":
            # iOS displays AR content natively on direct link access.
            # For a later process in project, other messaging apps can display webview inside the chat.
            # So there won't be any need to develop a wrapper for AR objects.
            itemDescription += f"<a href='{ item['3DModel'] }'>View 3D Model</a> \n"
        itemDescription += f"PRICE: { str(item['price'] / 100) } { item['currency'] }"
        
        buttonsInMenuItem = [
            "_pay&" + item["id"], # Payment button for item
            "<" + venueKey # Go back item
            ]
            
        #     [InlineKeyboardButton("Order and Pay Now", callback_data = "pay", pay=True)],
        #     [InlineKeyboardButton(upMenuStr, callback_data = "<" + venueKey]
        # ]

        
        markups[itemKey] = {
            "name": item["name"],
            "text": itemDescription,
            "children": buttonsInMenuItem
        }
    
    # TODO pass/implement parent category
    menuArray.append("<food")
    
    venueDescription = f"""
    <a href='{venue['image'] } '>·</a>
    <b> {venue['name'].upper()} </b>
    Score: {venue['score']}
    Address: { venue['address'] }
    Phone: <a href='tel:{ venue['phone'] }'>{ venue['phone'] }</a>
    """
    
    # TODO: Calculate real distance from user's location.
    distance = random.choice([100, 250, 300, 400, 500])
    
    markups[venueKey] = {
        "text": venueDescription,
        "name": venue["name"] + " " + venue["score"] + "⭐️ - " + str(distance) + " meters",
        "children": menuArray
    }
    
    print(markups)

# def view_button_venues_in_category(crntPath : str):
#     type = lastPathParam(crntPath)
#     keyboard = []
#     for venue in model.venueModel.venues:
#         keyboard.append( [InlineKeyboardButton(venue["name"], callback_data = addToPath(crntPath, venue["id"]))] )
#     keyboard.append( [InlineKeyboardButton(f"Other {type}s", callback_data = "main")] )
#     keyboard.append( [InlineKeyboardButton(upMenuStr, callback_data = prvPath(crntPath))] )
#     return InlineKeyboardMarkup(keyboard)

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
    
    return InlineKeyboardMarkup(keyboard)

