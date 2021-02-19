import pytest


@pytest.fixture()
def one_set_up():
    print("before every tests")
    yield
    print("after every tests")
