from utils.envUtils import ENV

headers = {
    'Square-Version': '2023-05-17',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ENV.SQUARE_TOKEN_SANDBOX
    }

baseUrl = "https://connect.squareupsandbox.com/v2"

locationsEndpoint = baseUrl + "/locations/"
catalogEndpoint = baseUrl + "/catalog/list/"
ordersEndpoint = baseUrl + "/orders/"
paymentsEndpoint = baseUrl + "/payments/"
catalogObjectEndpoint = baseUrl + "/catalog/object/"
customersEndpoint = baseUrl + "/customers/"
