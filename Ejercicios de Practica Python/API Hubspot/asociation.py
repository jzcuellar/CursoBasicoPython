# import hubspot
# from pprint import pprint
# from hubspot.crm.objects.notes import ApiException

# client = hubspot.Client.create(access_token="pat-na1-56f2f1f9-b111-466e-a5e0-82b0e1b879be")

# try:
#     api_response = client.crm.objects.notes.associations_api.create(note_id=28846872190, to_object_type="contact", to_object_id=101, association_spec=[{"associationCategory":"HUBSPOT_DEFINED"}])
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling associations_api->create: %s\n" % e)



# # OPCION 2

import requests

# url = "https://api.hubapi.com/crm/v3/objects/notes/{noteId}/associations/{toObjectType}/{toObjectId}/{associationType}"

url = "https://api.hubapi.com/crm/v3/objects/notes/28846872190/associations/contact/101/202"

payload = "[{\"associationCategory\":\"HUBSPOT_DEFINED\",\"associationTypeId\":0}]"
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': "pat-na1-56f2f1f9-b111-466e-a5e0-82b0e1b879be" # Code
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)