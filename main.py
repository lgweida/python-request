import requests
import json

FETCH_API = os.env.get('FETCH_URL')
res = requests.get(FETCH_API)

json_object = res.json()

json_formatted_str = json.dumps(json_object, indent=2)

print(json_formatted_str)

#print(res.json())
