import requests

base_url = 'http://localhost:5000/api'


response = requests.post(base_url, json={'name': 'Musa Parsanka'})
print(response.json())

# Fetch details of a person
user_id = response.json().get('id')
response = requests.get(f'{base_url}/{user_id}')
print(response.json())

# Modify the details of an existing person
response = requests.put(f'{base_url}/{user_id}', json={'name': 'New Name'})
print(response.json())

# Remove a person
response = requests.delete(f'{base_url}/{user_id}')
print(response.json())
