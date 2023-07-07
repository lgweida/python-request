import requests
import json

res = requests.get("http://129.213.18.27:5010/")

json_object = res.json()

json_formatted_str = json.dumps(json_object, indent=2)

print(json_formatted_str)

#print(res.json())