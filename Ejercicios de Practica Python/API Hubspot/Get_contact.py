# GET CONTACT 
from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput
from hubspot.crm.contacts.exceptions import ApiException
api_client = HubSpot(access_token='pat-na1-56f2f1f9-b111-466e-a5e0-82b0e1b879be')

try:
    contact_fetched = all_contacts = api_client.crm.contacts.get_all()
    print(contact_fetched)
except ApiException as e:
    print("Exception when requesting contact by id: %s\n" % e)

#GET NOTES
# import hubspot
# from pprint import pprint
# from hubspot.crm.objects.notes import ApiException

# client = hubspot.Client.create(access_token="pat-na1-56f2f1f9-b111-466e-a5e0-82b0e1b879be")

# try:
#     api_response = client.crm.objects.notes.basic_api.get_page(limit=10, archived=False)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling basic_api->get_page: %s\n" % e)