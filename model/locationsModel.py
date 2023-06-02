import requests
import json
from model.network import headers, locationsEndpoint
from model.venueModel import addVenue
from model.catalogModel import getMenu


def initLocations():
    response = requests.request("GET", locationsEndpoint, headers=headers, data="")
    if response.status_code == 200:
        locations = json.loads(response.text)["locations"]
        for location in locations:
            id = location["id"]
            name = location["name"]
            address = location["address"]["address_line_1"]
            phone = location["phone_number"]
            image = ""
            if location.__contains__("pos_background_url"):   
                image = location["pos_background_url"]
            menu = getMenu()
            
            addVenue(id=id, name=name, address=address, phone=phone, image=image, menu=menu)
