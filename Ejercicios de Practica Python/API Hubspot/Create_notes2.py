import hubspot
from pprint import pprint
from hubspot.crm.objects.notes import SimplePublicObjectInput, ApiException

client = hubspot.Client.create(access_token="pat-na1-56f2f1f9-b111-466e-a5e0-82b0e1b879be")

properties = {
    "hs_timestamp": "2022-12-11T03:30:17.883Z",
    "hs_note_body":
        'Created date 17/01/2021'
        'Street Address Blackheath  Vale, 8448'
        'Industry Meat'
}
simple_public_object_input = SimplePublicObjectInput(properties=properties)
try:
    api_response = client.crm.objects.notes.basic_api.create(simple_public_object_input=simple_public_object_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling basic_api->create: %s\n" % e)