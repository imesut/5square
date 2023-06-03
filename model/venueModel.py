import random

from utils.envUtils import ENV

venues = [
    # {
    #     "id": "1002",
    #     "name": "The 5quare Restaurant",
    #     "address": "Random Street, Number 3/5",
    #     "phone": "1234-567-8901",
    #     "score": "3.5/5",
    #     "description": "Visual description will come here.",
    #     "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSCMa9b83vLTLq3g5mcPHi9DLUeMhlLbyLbQ&usqp=CAU",
    #     "menu": [
    #         {
    #             "id": "3001", 
    #             "name": "Pie Lemon Meringue",
    #             "price": 2.15,
    #             "currency": "USD",
    #             "3DModel": "https://developer.apple.com/augmented-reality/quick-look/models/meringue/pie_lemon_meringue.usdz",
    #             "image": "https://www.onceuponachef.com/images/2018/04/Lemon-Meringue-Pie-1.jpg"
    #         },
    #         {
    #             "id": "3002", 
    #             "name": "Burger Awesome",
    #             "price": 7.49,
    #             "currency": "USD",
    #             "3DModel": "",
    #             "image": "https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/102cf51c-9220-4278-8b63-2b9611ad275e/Derivates/3831dbe2-352e-4409-a2e2-fc87d11cab0a.jpg"
    #         },
    #         {
    #             "id": "3003",
    #             "name": "Lemonade",
    #             "price": 1.49,
    #             "currency": "USD",
    #             "3DModel": "",
    #             "image": "https://www.simplyrecipes.com/thmb/4LFrc9hSMoKErr2WI7tThcnvWwA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Perfect-Lemonade-LEAD-08-B-441ceb568f854bb485dbed79e082bb4a.jpg"
    #         }
    #     ]
    # },
    {
        "id": "1003",
        "name": "Chief's Pizza",
        "address": "Awesome Street, Number 5/5",
        "score": "3.5/5",
        "phone": "9876543210",
        "description": "Visual description will come here.",
        "image": "https://d332juqdd9b8hn.cloudfront.net/wp-content/uploads/2019/04/BEAUTIFULPIZZERIA.jpg",
        "menu": [
            {
                "id": "4001",
                "name": "Pizza Margherita (Gluten Free)",
                "price": 12.50,
                "currency": "USD",
                "3DModel": "",
                "image": "https://cookieandkate.com/images/2021/07/classic-margherita-pizza.jpg",
                "gluten_free": True,
                "lactose_free": False,
                "vegetarian": False,
                "ingredients": "A, B, C, D"
            },
            {
                "id": "4002",
                "name": "Pizza Margherita",
                "price": 12.50,
                "currency": "USD",
                "3DModel": "",
                "image": "https://cookieandkate.com/images/2021/07/classic-margherita-pizza.jpg",
                "gluten_free": False,
                "lactose_free": False,
                "vegetarian": False,
                "ingredients": "A, B, C, D"
            },
            {
                "id": "4003",
                "name": "Pizza Pepperoni",
                "price": 17.50,
                "currency": "USD",
                "3DModel": "",
                "image": "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F19%2F2014%2F07%2F10%2Fpepperoni-pizza-ck-x.jpg&q=60",
                "gluten_free": False,
                "lactose_free": False,
                "vegetarian": False,
                "ingredients": "A, B, C, D"
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
