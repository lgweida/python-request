import requests
import json
import os

FETCH_API = os.environ['FETCH_URL']

res = requests.get(FETCH_API)

json_object = res.json()

json_formatted_str = json.dumps(json_object, indent=2)

print(json_formatted_str)

#print(res.json())
