import requests

URL = "https://api.github.com/some/endpoint"
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(URL, headers=headers)
response.raise_for_status()
print(response.json())
