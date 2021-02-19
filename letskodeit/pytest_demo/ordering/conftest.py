import pytest


@pytest.fixture()
def set_up():
    print("before method")
    yield
    print("after method")


@pytest.fixture(scope="module")
def one_set_up(browser):
    if browser == "chrome":
        print("running test on chrome")
    elif browser == "ff":
        print("running test on firefox")
    yield
    print("after every test file")


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
