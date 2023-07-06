import requests
res = requests.get("http://129.213.18.27:5010/")
print(res.json())