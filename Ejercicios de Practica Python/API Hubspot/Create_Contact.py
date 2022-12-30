from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput
from hubspot.crm.contacts.exceptions import ApiException
api_client = HubSpot(access_token='pat-na1-56f2f1f9-b111-466e-a5e0-82b0e1b879be')

data_user = {
    'email': 'jack_nobbs136820696@hourpy.biz',
    'phone': '(+44) 1043 56031',
    'address': 'Carol   Way, 7139',
    'country': 'England',
    'industry': 'Meat'
}

try:
    simple_public_object_input = SimplePublicObjectInput(
        properties=(data_user)
    )
    api_response = api_client.crm.contacts.basic_api.create(
        simple_public_object_input=simple_public_object_input
    )
except ApiException as e:
    print("Exception when creating contact: %s\n" % e)