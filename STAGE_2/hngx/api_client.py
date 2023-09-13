# api_client.py

import requests

url = "http://localhost:5000/api"
headers = {"Content-Type": "application/json"}
data = {"name": "John Doe"}

response = requests.post(url, headers=headers, json=data)
