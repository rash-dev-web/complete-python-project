import pytest


@pytest.mark.order(after="test_method_sample")
def test_method_one(one_set_up, set_up):
    print("test method one")


def test_method_sample():
    print("sample")


@pytest.mark.order(before="test_method_sample")
def test_method_two(one_set_up, set_up):
    print("test method two")
