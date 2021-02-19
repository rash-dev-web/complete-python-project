import requests


s = requests.Session()
s.get("https://httpbin.org/cookies/set/sessioncookie/123456789")
r = s.get("https://httpbin.org/cookies")
print(r.text)


# default data

s = requests.Session()
s.auth = ("user", "pass")
s.headers.update({"x-test": "true"})
r = s.get("https://httpbin.org/headers", headers={"x-test2": "true"})
print(r.text)

# method-level parameters will not be persisted across requests
s = requests.Session()
r = s.get("https://httpbin.org/cookies", cookies={"from-my": "browser"})
print(r.text)

r = s.get("https://httpbin.org/cookies")
print(r.text)

