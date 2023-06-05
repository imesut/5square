import random

from utils.envUtils import ENV

venues = [
    {
        "id": "1003",
        "name": "Coffee Public",
        "address": "Coffee Street Number 5/5",
        "score": "3.5/5",
        "phone": "9876543210",
        "description": "Coffee Public is a small sweet spot located on a wide street, with a few small tables in front and a cash register on the right side upon entering. In front of coffee, you'll find a cozy atmosphere with around 3-4 tables. It doesn't appear crowded based on the photos. The place mainly specializes in desserts and coffee, which are the standout items.",
        "image": "https://github.com/atakan-nalbant/hackathonimages/blob/main/coffeepublic.jpg?raw=true",
        "menu": [
            {
                "id": "4001",
                "name": "Lemon Cheesecake",
                "price": 7.99,
                "currency": "USD",
                "3DModel": "",
                "image": "https://github.com/atakan-nalbant/hackathonimages/blob/main/Lemon%20Cheesecake.jpg?raw=true",
                "gluten_free": True,
                "lactose_free": False,
                "vegetarian": True,
                "ingredients": "Cream cheese, Digestive biscuit crust, Lemon zest, Lemon juice"
            },
            {
                "id": "4002",
                "name": "Chocolate Chip Cookie",
                "price": 14.99,
                "currency": "USD",
                "3DModel": "",
                "image": "https://github.com/atakan-nalbant/hackathonimages/blob/main/Chocolate%20Chip%20Cookie.jpg?raw=true",
                "gluten_free": False,
                "lactose_free": False,
                "vegetarian": True,
                "ingredients": "Chocolate Chips, Butter, Gluten Free Flour, Brown sugar, White sugar, Sea Salt"
            },
            {
                "id": "4003",
                "name": "Latte",
                "price": 4.99,
                "currency": "USD",
                "3DModel": "https://raw.githubusercontent.com/atakan-nalbant/hackathonimages/main/latte%203d.usdz",
                "image": "https://github.com/atakan-nalbant/hackathonimages/blob/main/latte%202.jpg?raw=true",
                "gluten_free": True,
                "lactose_free": True,
                "vegetarian": True,
                "ingredients": "Espresso shot, steamed milk, frothed milk."
            }
        ]
    }
]


def addVenue(id, name, address, phone, image, description, menu):
    
    venues.append({
        "id": id,
        "name": name,
        "address": address,
        "phone": phone,
        "image": image,
        "description": description,
        "menu" : menu,
        "score": random.choice(["5/5", "4.5/5", "4/5"]) # Implement a rating and rate update system in future.
    })
    
def getVenue(id):
    for venue in venues:
        if venue["id"] == id:
            return venue

def getItem(venue, item_id):
    for item in venue["menu"]:
        if item["id"] == item_id:
            return item

# No function overload in Python, so define a new name
def getItemWoVenue(item_id):
    for venue in venues:
        for item in venue["menu"]:
            if item["id"] == item_id:
                return item

# No function overload in Python, so define a new name
def getVenueId(item_id : str) -> str:
    """
    Args:
        item_id (str): item's id

    Returns:
        str: venue=location's id
    """
    for venue in venues:
        for item in venue["menu"]:
            if item["id"] == item_id:
                return venue["id"]
