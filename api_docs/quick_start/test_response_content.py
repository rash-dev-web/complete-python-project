import requests


response = requests.get("https://api.github.com/events")
print(type(response.text))
print(response.headers)
