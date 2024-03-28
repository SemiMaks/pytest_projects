import pytest


@pytest.fixture
def my_fruit():
    yield "apple"


@pytest.fixture
def fruit_basket(my_fruit):
    return ["banana", "apple"]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
    print("Фрукты в порядке!")
