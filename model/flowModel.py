from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import model.venueModel

import utils.prefUtils
import random

upMenuStr = "👆 Go to the Previous Menu"

markups = {
    "main": {
        "text": "<b>Welcome to AllSquare.</b>\nYou can shop at places that provide payment infrastructure and offer you a personalized experience with the Square platform.",
        "name": "Main Menu",
        "children": [ "categories_ask_location", "venue_preferences", "food_preferences", "learn_more" ]
    },
    "categories_ask_location": {
        "text": "<b>Please share your location.</b>",
        "name": "List Nearby Places",
        "children": [ "<main" ]
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
        "children": [ "food_preferences&vegetarian", "food_preferences&gluten_allergy", "food_preferences&lactose_allergy", "food_preferences&other_allergy", "<main" ]
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
    "lactose_allergy": { "name": "Choose lactose-free options" },
    "other_allergy": { "name": "I have another allergy" },
    "learn_sign_language": {
        "text": """<b>Discover how to order with sign language</b>
        Explore sample sign language images or ask our assistants, pick one below.""",
        "name": "Discover how to order with sign language",
        "children": [ "sign_lang_can_i_have", "sign_lang_thanks", "sign_lang_please", "<main" ]
    },
    "sign_lang_can_i_have": {
        "text": """
        <b>Can I have?</b>
        <a href='https://8designers.com/blog/bl-content/uploads/pages/d1d6f72feff040a9a81d9dc06a3b366d/Wow-gif.gif'>·</a>
        <b>Description:</b> Place your hands like...
        """,
        "name": "Can I have ...?",
        "children": [ "<learn_sign_language" ]
    },
    "sign_lang_thanks": {
        "text": """
        <b>Thanks</b>
        <a href='https://8designers.com/blog/bl-content/uploads/pages/d1d6f72feff040a9a81d9dc06a3b366d/Wow-gif.gif'>·</a>
        <b>Description:</b> Place your hands like...
        """,
        "name": "Thanks",
        "children": [ "<learn_sign_language" ]
    },
    "sign_lang_please": {
        "text": """
        <b>Please</b>
        <a href='https://8designers.com/blog/bl-content/uploads/pages/d1d6f72feff040a9a81d9dc06a3b366d/Wow-gif.gif'>·</a>
        <b>Description:</b> Place your hands like...
        """,
        "name": "Please",
        "children": [ "<learn_sign_language" ]
    }
}

def insertItemsToFlow():
    for venue in model.venueModel.venues:
        venueKey = "venue=" + venue["id"]
        menuArray = []
        
        for item in venue["menu"]:
            itemKey = "item=" + item["id"]
            menuArray.append( itemKey )
            
            """
            Add Item Description Text to the Message
            """
            itemDescription = f"<b> { venue['name'].upper() } </b> \n"
            if item["image"] != "":
                itemDescription += f"<a href='{ item['image'] }'>·</a> \n"
            if item["3DModel"] != "":
                # iOS displays AR content natively on direct link access.
                # For a later process in project, other messaging apps can display webview inside the chat.
                # So there won't be any need to develop a wrapper for AR objects.
                itemDescription += f"<a href='{ item['3DModel'] }'>View 3D Model</a> \n"
            if item["ingredients"] != "":
                itemDescription += f"<b>Ingredients:</b> { item['ingredients'] }\n"
            itemDescription += f"<b>PRICE:</b> { str(item['price'] ) } { item['currency'] }"
            
            
            buttonsInMenuItem = [
                "_pay&" + item["id"], # Payment button for item
                "learn_sign_language",
                "<food_preferences",
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
        menuArray.append("<food_preferences")
        menuArray.append("<food")
        
        """
        Add Venue Description Text to the Message
        """
        venueDescription = f"""
        <a href='{venue['image'] } '>·</a>
        <b> {venue['name'].upper()} </b> Score: {venue['score']}
        {venue['description']}
        <i>
        Address: { venue['address'] }
        Phone: <a href='tel:{ venue['phone'] }'>{ venue['phone'] }</a>
        </i>
        """
        
        # TODO: Calculate real distance from user's location.
        distance = random.choice([100, 250, 300, 400, 500])
        
        markups[venueKey] = {
            "text": venueDescription,
            "name": venue["name"] + " " + venue["score"] + "⭐️ - " + str(distance) + " meters",
            "children": menuArray
        }
        
        print(markups)
