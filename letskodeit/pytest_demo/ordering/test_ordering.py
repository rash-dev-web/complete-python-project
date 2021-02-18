import pytest


def test_method_one(one_set_up, set_up):
    print("test method one")


@pytest.mark.order("first")
def test_method_two(one_set_up, set_up):
    print("test method two")


@pytest.mark.order(index=-2)
def test_method_three(one_set_up, set_up):
    print("test method three")


@pytest.mark.order(1)
def test_method_four(one_set_up, set_up):
    print("test method four")
