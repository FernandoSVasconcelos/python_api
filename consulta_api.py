import requests

req = requests.get(f"http://192.168.0.17:5000/api?page={2}")
print(req.json())