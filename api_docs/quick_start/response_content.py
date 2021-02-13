import requests


response = requests.get("https://api.github.com/events", stream=True)

# content of the server response
# print(response.text)

# encoding type
# print(response.encoding)

# binary response, access the response body as bytes, for non-text requests:
# print(response.content)
#
# # json response content
# print(response.json())
#
# # to check a request is successful
# response.raise_for_status()

# raw response content
print(response.raw)
print(response.raw.read(10))
