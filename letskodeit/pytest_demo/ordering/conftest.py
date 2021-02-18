import pytest


@pytest.fixture()
def set_up():
    print("before method")
    yield
    print("after method")


@pytest.fixture(scope="module")
def one_set_up():
    print("before every test file")
    yield
    print("after every test file")
