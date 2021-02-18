import requests

response = requests.get("http://github.com")
print(response.url)
print(response.status_code)
print(response.history)

# disable redirect
response = requests.get("http://github.com", allow_redirects=False)
print(response.status_code)
print(response.history)

# enable redirect for head request
response = requests.head("http://github.com", allow_redirects=True)
print(response.status_code)
print(response.history)

