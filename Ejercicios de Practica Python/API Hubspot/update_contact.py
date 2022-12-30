import hubspot
from pprint import pprint
from hubspot.crm.contacts import SimplePublicObjectInput, ApiException

client = hubspot.Client.create(access_token="pat-na1-56f2f1f9-b111-466e-a5e0-82b0e1b879be")

properties = {
    'firstname': 'Owen',
    'lastname': 'Wigley',
    'address': 'Dunstable   Alley, 1437'
}
simple_public_object_input = SimplePublicObjectInput(properties=properties)
try:
    api_response = client.crm.contacts.basic_api.update(contact_id="101", simple_public_object_input=simple_public_object_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling basic_api->update: %s\n" % e)