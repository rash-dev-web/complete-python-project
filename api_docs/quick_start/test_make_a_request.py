# import pytest
import requests


def test_get():
    response = requests.get("https://api.github.com/events")
    print(f"Response : {response}")


def test_post():
    response = requests.post("https://httpbin.org/post", data={"key": "value"})
    print(f"Response : {response}")


def test_put():
    response = requests.put("https://httpbin.org/put", data={"key": "value"})
    print(f"Response : {response}")


def test_delete():
    response = requests.delete("https://httpbin.org/delete")
    print(f"Response : {response}")


def test_head():
    response = requests.head("https://httpbin.org/get")
    print(f"Response : {response}")


def test_options():
    response = requests.options("https://httpbin.org/get")
    print(f"Response : {response}")
