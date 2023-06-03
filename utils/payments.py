from telegram import Update

from model.venueModel import *
from model.squareModels.customerModel import findOrCreateCustomer
from model.squareModels.orderModel import orderItem

def payItem(update : Update, itemId : str) -> str:    
    """
    Pays item, handles all of the works

    Returns:
        str : receiptNumber as a string, returns "-1" if there is a problem.
    """

    user = update.callback_query.from_user    
    # t.me link is the id to be used
    userName = user.link
    userName = userName[(userName.find("t.me")+5):] # Cleaning prefixes
    
    venueId = getVenueId(item_id = itemId)
    customerId = findOrCreateCustomer(userName = userName, name = user.first_name, surname = user.last_name)
    receiptNumber = orderItem(locationId = venueId, catalog_object_id = itemId, customerId = customerId) if customerId != "" else "-1"
    
    return receiptNumber
