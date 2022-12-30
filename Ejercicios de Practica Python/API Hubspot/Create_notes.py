# properties = {
#     'id': '101',
#     "firstdealcreateddate": "2021-01-17 09:25:07",
#     "address": "Blackheath Vale, 8448",
#     "industry": "Meat"
# }

import requests
import json

# url = "/crm/v3/objects/notes/{noteId}/associations/{toObjectType}/{toObjectId}/{associationType}"  EStructura Basica para PUT Request Idea hacer un for

url = "https://api.hubapi.com/crm/v3/objects/notes/1/associations/contact/101/202"

querystring = {"hapikey":"pat-na1-56f2f1f9-b111-466e-a5e0-82b0e1b879be"}

payload = json.dumps({
    "metadata": {
            'id': '101',
            "firstdealcreateddate": "2021-01-17 09:25:07",
            "address": "Blackheath Vale, 8448",
            "industry": "Meat"
    }
});
headers = {
    'Content-Type': "application/json",
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)