from utils.pathUtils import *
import model.venueModel

def textForPath(path : str) -> str:
    array = splitPathStr(path)
    text = ""
    
    if len(array) == 1:
        return "<b>Welcome to The 5Quare Bot!</b>"
    
    if len(array) == 2:
        # Categories
        if array[1] == "vn_ctgs":
            return "<b>CATEGORIES</b>"
        # LEARN MORE
        elif array[1] == "l_m":
            # TODO
            return "TODO: ADD a Learn More text!\n\n"*5
        elif array[1] == "venue_preferences":
            return "<b>VENUE PREFERENCES</b>\nPlease select criterias to filter venues."
    
    if len(array) == 3:
        if array[1] == "vn_ctgs":
            return f"<b>NEARBY { array[-1].upper() } VENUES</b>" # This is the Category name
    
    if len(array) == 4:
        # Venue Details
        if array[1] == "vn_ctgs":
            venue_id = array[-1]
            venue = getVenue(venue_id)
            text += f"<a href='{venue['image'] } '>·</a> \n"
            text += f"<b> {venue['name'].upper()} </b> \n"
            text += f"Score: {venue['score']} \n"
            text += f"Address: { venue['address'] } \n"
            text += f"Phone: <a href='tel:{ venue['phone'] }'>{ venue['phone'] }</a> \n"
            return text
    
    elif len(array) == 5:
        # Menu Item Details
        if array[1] == "vn_ctgs":
            venue_id = array[-2]
            venue = getVenue(venue_id)
            return f"<b>{ venue['name'].upper() }</b>"
    
    elif len(array) == 6:
        # Menu Item Details
        if array[1] == "vn_ctgs":
            venue_id = array[-3]
            item_id = array[-1]
            # find the model
            venue = getVenue(venue_id)
            item = getItem(venue, item_id)
            text += f"<b> { venue['name'].upper() } </b> \n"
            text += f"<b> { item['name'].upper() } </b> \n"
            if item["image"] != "":
                text += f"<a href='{ item['image'] }'>·</a> \n"
            if item["3DModel"] != "":
                text += f"<a href='{ item['3DModel'] }'>View 3D Model</a> \n"
            text += f"PRICE: { str(item['price']) } { item['currency'] }"
            return text
    else:
        return "path"


def getVenue(id):
    for venue in model.venueModel.venues:
        if venue["id"] == id:
            return venue

def getItem(venue, item_id):
    for item in venue["menu"]:
        if item["id"] == item_id:
            return item

