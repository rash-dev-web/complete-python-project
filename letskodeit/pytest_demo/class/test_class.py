import pytest


@pytest.mark.usefixtures("one_set_up")
class TestDemoClass:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("setup")

    def test_method_one(self):
        print("method one")

    def test_method_two(self):
        print("method two")
