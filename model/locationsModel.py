import requests
import json
from network import headers, locationsEndpoint

def getLocations():
    response = requests.request("GET", locationsEndpoint, headers=headers, data="")
    if response.status_code == 200:
        locations = json.loads(response.text)["locations"]
        for location in locations:
            location["id"]
            location["name"]
            location["address"]["address_line_1"]
            location["phone_number"]
            if location.__contains__("pos_background_url"):   
                image = location["pos_background_url"]
            else:
                image = ""
