import pytest


@pytest.fixture()
def set_up():
    print("before every method...")
    yield
    print("after every method...")


@pytest.fixture(scope="module")
def one_set_up():
    print("before every test file")
    yield
    print("after every test file")
