import hubspot
from pprint import pprint
from hubspot.crm.objects.notes import ApiException

client = hubspot.Client.create(access_token="pat-na1-56f2f1f9-b111-466e-a5e0-82b0e1b879be")

try:
    api_response = client.crm.objects.notes.basic_api.archive(note_id='28846502667')
    pprint(api_response)
except ApiException as e:
    print("Exception when calling basic_api->archive: %s\n" % e)