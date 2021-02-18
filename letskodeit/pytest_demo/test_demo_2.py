import pytest


@pytest.fixture()
def set_up():
    print("before test...")
    yield
    print("after test...")


def test_method_one(set_up):
    print("method one...")


def test_method_two(set_up):
    print("method two...")
