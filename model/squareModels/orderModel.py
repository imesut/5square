import requests
import json
import time
from network import headers, ordersEndpoint, paymentsEndpoint


def orderItem(locationId : str, catalog_object_id : str, userName : str, customerId : str) -> str:
    """Places order of the user.

    Args:
        locationId (str): venue's Id
        catalog_object_id (str): item id, should be as variation id

    Returns:
        str : receiptNumber as a string, returns "-1" if there is a problem.
    """
    idempotencyKey = "TG-5QUARE" + str(time.time())
    
    payload = json.dumps({
        "order": {
            "location_id": locationId,
            "customer_id": customerId,
            "line_items": [
                {
                    "quantity": "1", # Single item for the POC reasons to simplify flow and focus on the main thing.
                    "catalog_object_id": catalog_object_id
                }
            ],
            "pricing_options": {
                "auto_apply_discounts": True,
                "auto_apply_taxes": True
            }
            "fulfillments": [
                {
                    "type": "PICKUP",
                    "state": "PROPOSED",
                    "pickup_details": {
                        "schedule_type": "ASAP",
                        "prep_time_duration": "P30M",
                        "recipient": {
                            "customer_id": customerId
                        }
                    }
                }
            ]
        },
        "idempotency_key": idempotencyKey
        })
    
    response = requests.request("POST", ordersEndpoint, headers = headers, data = payload)
    
    if response.status_code == 200:    
        response = json.loads(response.text)
        orderId = response["order"]["id"]
        amount = response["net_amount_due_money"]["amount"]
        currency = response["net_amount_due_money"]["currency"]
        receiptNumber = payOrder(idempotencyKey=idempotencyKey, orderId=orderId, amount=amount, currency=currency)
        return receiptNumber
    else:
        return "-1"

# Sample Order Function Call
# orderItem("L7E1Z2CGNYTM8", "5LN4DYZESGUI2ZLS3ZP6GY4S", "Mesut Yılmaz", "mesuts_telegram_id")

def payOrder(idempotencyKey : str, orderId : str, amount : int, currency : str) -> str:

    payload = json.dumps({
        "idempotency_key": idempotencyKey,
        "source_id": "CASH", # Hack for hackathon - The reaason of this will be explained in the documentation.
        "cash_details": {
            "buyer_supplied_money": {
                "amount": amount,
                "currency": currency
            }
        },
        "amount_money": {
            "amount": amount,
            "currency": currency
        },
        "order_id": orderId
    })

    response = requests.request("POST", paymentsEndpoint, headers=headers, data=payload)
    
    if response.status_code == 200:
        response = json.loads(response.text)
        receiptNumber = response["payment"]["receipt_number"]
        paymentId = response["payment"]["id"]
        if completeOrder(paymentId=paymentId) == 200:
            return receiptNumber
        else:
            return "-1"


def completeOrder(paymentId : str) -> int:
    url = paymentsEndpoint + paymentId + "/complete"
    response = requests.request("POST", url, headers=headers, data="")
    
    return response.status_code
