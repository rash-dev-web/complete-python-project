import requests


def test_pass_param():
    payload = {'key1': 'value1', 'key2': 'value2'}
    response = requests.get("https://httpbin.org/get", params=payload)
    print(response.url)


def test_pass_param_two():
    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    response = requests.get("https://httpbin.org/get", params=payload)
    print(response.url)
