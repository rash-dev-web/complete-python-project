import requests


r = requests.get("https://en.wikipedia.org/wiki/Monty_Python")
print(r.headers)
print(r.request.headers)
