import requests

req = requests.get(f"http://192.168.0.17:5000/api?page={6}")
print(req.json())

req = requests.get(f"http://192.168.0.17:5000/db?page={1}")
print(req.json())