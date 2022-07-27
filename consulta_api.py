import requests

req = requests.get("http://192.168.0.17:5000/api")
print(req.json())