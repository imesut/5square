from model.squareModels.network import headers, customersEndpoint
import requests, json


def findOrCreateCustomer(userName : str, name : str, surname : str) -> str:
    idFromSearch = searchCustomer(userName=userName)
    
    if idFromSearch == "":
        return createCustomer(name=name, surname=surname, userName=userName)
    else:
        return idFromSearch

def searchCustomer(userName : str) -> str:
    res = requests.request("POST", customersEndpoint + "search", headers=headers, data=json.dumps({"query": {
        "filter": {
            "reference_id": { "exact": "t.me/" + userName }
            }}}))
    
    if res.status_code == 200:
        res = json.loads(res.text)
        if res.__contains__("customers"):
            customer = res["customers"][0]
            return customer["id"]
    else:
        return ""

def createCustomer(name : str, surname : str, userName : str) -> str:
    data = json.dumps({
        "given_name": name,
        "family_name": surname,
        "reference_id": "t.me/" + userName
    })
    
    response = requests.request("POST", customersEndpoint, headers=headers, data=data)
        
    if response.status_code == 200:
        customer = json.loads(response.text)["customer"]
        return customer["id"]
    else:
        return ""