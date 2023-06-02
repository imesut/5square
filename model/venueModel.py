import json
from utils.envUtils import ENV

response = """
{
    "objects": [
        {
            "type": "CUSTOM_ATTRIBUTE_DEFINITION",
            "id": "N7DOEXKDO2QP674PXNUB56JB",
            "updated_at": "2023-05-29T18:16:56.758Z",
            "created_at": "2023-05-29T18:16:56.758Z",
            "version": 1685384216758,
            "is_deleted": false,
            "present_at_all_locations": true,
            "custom_attribute_definition_data": {
                "type": "BOOLEAN",
                "name": "vegetarian",
                "source_application": {
                    "application_id": "Square"
                },
                "allowed_object_types": [
                    "ITEM",
                    "ITEM_VARIATION"
                ],
                "seller_visibility": "SELLER_VISIBILITY_READ_WRITE_VALUES",
                "app_visibility": "APP_VISIBILITY_READ_WRITE_VALUES",
                "key": "81ea0b74-8978-45f8-93e1-644b9d887d6d"
            }
        },
        {
            "type": "ITEM",
            "id": "GS5YDGBOQCI47ESG6QWPJT5L",
            "updated_at": "2023-05-29T18:27:33.761Z",
            "created_at": "2023-05-29T18:16:57.646Z",
            "version": 1685384853761,
            "is_deleted": false,
            "custom_attribute_values": {
                "Square:25aeb5ca-d36c-4b41-8921-a0a6f484256b": {
                    "name": "3DModel",
                    "string_value": "https://developer.apple.com/augmented-reality/quick-look/models/meringue/pie_lemon_meringue.usdz",
                    "custom_attribute_definition_id": "OZOW5LPTO23PO2LIBPSST5RC",
                    "type": "STRING",
                    "key": "Square:25aeb5ca-d36c-4b41-8921-a0a6f484256b"
                },
                "Square:81ea0b74-8978-45f8-93e1-644b9d887d6d": {
                    "name": "vegetarian",
                    "custom_attribute_definition_id": "N7DOEXKDO2QP674PXNUB56JB",
                    "type": "BOOLEAN",
                    "boolean_value": true,
                    "key": "Square:81ea0b74-8978-45f8-93e1-644b9d887d6d"
                }
            },
            "present_at_all_locations": true,
            "item_data": {
                "name": "Pie Lemon Meringue",
                "is_taxable": true,
                "visibility": "PRIVATE",
                "variations": [
                    {
                        "type": "ITEM_VARIATION",
                        "id": "446OPJ6RTDQEA5HHAOE6A2PW",
                        "updated_at": "2023-05-29T18:22:40.628Z",
                        "created_at": "2023-05-29T18:16:57.646Z",
                        "version": 1685384560628,
                        "is_deleted": false,
                        "custom_attribute_values": {
                            "Square:81ea0b74-8978-45f8-93e1-644b9d887d6d": {
                                "name": "vegetarian",
                                "custom_attribute_definition_id": "N7DOEXKDO2QP674PXNUB56JB",
                                "type": "BOOLEAN",
                                "boolean_value": true,
                                "key": "Square:81ea0b74-8978-45f8-93e1-644b9d887d6d"
                            }
                        },
                        "present_at_all_locations": true,
                        "item_variation_data": {
                            "item_id": "GS5YDGBOQCI47ESG6QWPJT5L",
                            "name": "Regular",
                            "ordinal": 1,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 215,
                                "currency": "USD"
                            },
                            "track_inventory": false,
                            "sellable": true,
                            "stockable": true
                        }
                    }
                ],
                "product_type": "REGULAR",
                "skip_modifier_screen": false,
                "ecom_visibility": "UNINDEXED",
                "image_ids": [
                    "IWKSFUVH5LPABBSCSY5SBIKS"
                ]
            }
        },
        {
            "type": "CUSTOM_ATTRIBUTE_DEFINITION",
            "id": "OZOW5LPTO23PO2LIBPSST5RC",
            "updated_at": "2023-05-29T18:27:33.399Z",
            "created_at": "2023-05-29T18:27:33.399Z",
            "version": 1685384853399,
            "is_deleted": false,
            "present_at_all_locations": true,
            "custom_attribute_definition_data": {
                "type": "STRING",
                "name": "3DModel",
                "source_application": {
                    "application_id": "Square"
                },
                "allowed_object_types": [
                    "ITEM",
                    "ITEM_VARIATION"
                ],
                "seller_visibility": "SELLER_VISIBILITY_READ_WRITE_VALUES",
                "app_visibility": "APP_VISIBILITY_READ_WRITE_VALUES",
                "string_config": {
                    "enforce_uniqueness": false
                },
                "key": "25aeb5ca-d36c-4b41-8921-a0a6f484256b"
            }
        },
        {
            "type": "ITEM",
            "id": "PFWGSRU55GAQIIH45LN3T4MM",
            "updated_at": "2023-05-29T19:04:28.965Z",
            "created_at": "2023-05-29T18:28:35.926Z",
            "version": 1685387068965,
            "is_deleted": false,
            "present_at_all_locations": true,
            "item_data": {
                "name": "Burger Awesome",
                "is_taxable": true,
                "visibility": "PRIVATE",
                "variations": [
                    {
                        "type": "ITEM_VARIATION",
                        "id": "5LN4DYZESGUI2ZLS3ZP6GY4S",
                        "updated_at": "2023-05-29T18:28:35.926Z",
                        "created_at": "2023-05-29T18:28:35.926Z",
                        "version": 1685384915926,
                        "is_deleted": false,
                        "present_at_all_locations": true,
                        "item_variation_data": {
                            "item_id": "PFWGSRU55GAQIIH45LN3T4MM",
                            "name": "Regular",
                            "ordinal": 1,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 749,
                                "currency": "USD"
                            },
                            "track_inventory": false,
                            "sellable": true,
                            "stockable": true
                        }
                    }
                ],
                "product_type": "REGULAR",
                "skip_modifier_screen": true,
                "ecom_visibility": "UNINDEXED",
                "image_ids": [
                    "ISW5SUXOQNMD477IYUS5I54F"
                ]
            }
        }
    ]
}
"""

venueObject = json.loads(response)

venues = [
    {
        "id": "1002",
        "name": "The 5quare Restaurant",
        "address": "Random Street, Number 3/5",
        "phone": "1234-567-8901",
        "score": "3.5/5",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSCMa9b83vLTLq3g5mcPHi9DLUeMhlLbyLbQ&usqp=CAU",
        "menu": [
            {
                "id": "3001", 
                "name": "Pie Lemon Meringue",
                "price": 2.15,
                "currency": "USD",
                "3DModel": "https://developer.apple.com/augmented-reality/quick-look/models/meringue/pie_lemon_meringue.usdz",
                "image": "https://www.onceuponachef.com/images/2018/04/Lemon-Meringue-Pie-1.jpg"
            },
            {
                "id": "3002", 
                "name": "Burger Awesome",
                "price": 7.49,
                "currency": "USD",
                "3DModel": "",
                "image": "https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/102cf51c-9220-4278-8b63-2b9611ad275e/Derivates/3831dbe2-352e-4409-a2e2-fc87d11cab0a.jpg"
            },
            {
                "id": "3003",
                "name": "Lemonade",
                "price": 1.49,
                "currency": "USD",
                "3DModel": "",
                "image": "https://www.simplyrecipes.com/thmb/4LFrc9hSMoKErr2WI7tThcnvWwA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Perfect-Lemonade-LEAD-08-B-441ceb568f854bb485dbed79e082bb4a.jpg"
            }
        ]
    },
    {
        "id": "1003",
        "name": "Chief's Pizza",
        "address": "Awesome Street, Number 5/5",
        "score": "3.5/5",
        "phone": "9876543210",
        "image": "https://d332juqdd9b8hn.cloudfront.net/wp-content/uploads/2019/04/BEAUTIFULPIZZERIA.jpg",
        "menu": [
            {
                "id": "4001",
                "name": "Pizza Margherita",
                "price": 12.5,
                "currency": "USD",
                "3DModel": "",
                "image": "https://cookieandkate.com/images/2021/07/classic-margherita-pizza.jpg"
            },
            {
                "id": "4002",
                "name": "Pizza Pepperoni",
                "price": 17.5,
                "currency": "USD",
                "3DModel": "",
                "image": "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F19%2F2014%2F07%2F10%2Fpepperoni-pizza-ck-x.jpg&q=60"
            }
        ]
    }
]


def addVenue():
    
    venues.append({
        "id": "LOCATION_ID",
        "name": "",
    })
    
    """
    {
        "id": "1002",
        "name": "The 5quare Restaurant",
        "address": "Random Street, Number 3/5",
        "phone": "1234-567-8901",
        "score": "3.5/5",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSCMa9b83vLTLq3g5mcPHi9DLUeMhlLbyLbQ&usqp=CAU",
        "menu": [
            {
                "id": "3001", 
                "name": "Pie Lemon Meringue",
                "price": 2.15,
                "currency": "USD",
                "3DModel": "https://developer.apple.com/augmented-reality/quick-look/models/meringue/pie_lemon_meringue.usdz",
                "image": "https://www.onceuponachef.com/images/2018/04/Lemon-Meringue-Pie-1.jpg"
            },
    """
    
    

    for objectInVenue in venueObject["objects"]:
        if objectInVenue["type"] == "ITEM":
            id = objectInVenue["id"]
            itemData = objectInVenue["item_data"]
            itemName = itemData["name"]
            
            print()
            print(itemName)
            
            if objectInVenue.__contains__("custom_attribute_values"):       
                propertyList = objectInVenue["custom_attribute_values"]
                print(propertyList)
                
                for property in propertyList:
                    propName = propertyList[property]["name"]
                    fieldName = propertyList[property]["type"].lower() + "_value"
                    propVal = propertyList[property][fieldName]
                    print(propName, propVal)
            
            for variation in itemData["variations"]:
                if variation["type"] == "ITEM_VARIATION":
                    data = variation["item_variation_data"]
                    price = data["price_money"]["amount"] / 100
                    currency = data["price_money"]["currency"]
                    
                    print(itemName, price, currency)



def getVenue(id):
    for venue in venues:
        if venue["id"] == id:
            return venue

def getItem(venue, item_id):
    for item in venue["menu"]:
        if item["id"] == item_id:
            return item
