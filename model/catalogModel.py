import requests
import json
from model.network import headers, catalogEndpoint, catalogObjectEndpoint
from model.venueModel import addVenue


def getMenu():
    response = requests.request("GET", catalogEndpoint, headers=headers, data="")
    
    if response.status_code == 200:
        objects = json.loads(response.text)["objects"]
        menu = transformCatalogToMenu(objects=objects)
        return menu

    
def transformCatalogToMenu(objects) -> list:
    menu = []
    
    for object in objects:
        if object["type"] == "ITEM":
            id = object["id"]
            itemData = object["item_data"]
            
            print(itemData)
            
            itemName = itemData["name"]
            modelUrl = ""
            image = ""
            props = {}
            
            if object.__contains__("custom_attribute_values"):       
                propertyList = object["custom_attribute_values"]
                
                
                for property in propertyList:
                    propName = propertyList[property]["name"]
                    fieldName = propertyList[property]["type"].lower() + "_value"
                    propVal = propertyList[property][fieldName]
                    props[propName] = propVal
            
            for variation in itemData["variations"]:
                if variation["type"] == "ITEM_VARIATION":
                    variation_id = variation["id"]
                    data = variation["item_variation_data"]
                    price = data["price_money"]["amount"] / 100
                    currency = data["price_money"]["currency"]
                    
                    menu.append({
                        "id": variation_id,
                        "name": itemName,
                        "price": price,
                        "currency": currency,
                        "3DModel": props["3DModel"] if props.__contains__("3DModel") else "",
                        "image": fetchImage(itemData["image_ids"][0]) if itemData.__contains__("image_ids") else ""
                    })

    return menu

def fetchImage(imageId) -> str:
    rsp = requests.request("GET", catalogObjectEndpoint + imageId, headers=headers, data="")
    resp = json.loads(rsp.text)
    print(rsp.text)
    return resp["object"]["image_data"]["url"] if rsp.status_code == 200 else ""
    