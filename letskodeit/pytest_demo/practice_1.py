import pytest


@pytest.fixture()
def set_up():
    print("before every method")
    yield
    print("after every method")


def test_method_a(set_up):
    print("test method A")


def test_method_b(set_up):
    print("test method B")

