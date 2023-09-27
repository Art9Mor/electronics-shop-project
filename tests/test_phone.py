import pytest

from src.phone import Phone


@pytest.fixture
def test_phone():
    return Phone("iPhone 14", 120000, 5, 2)


def test_phone_init(test_phone):
    assert len(test_phone.all) == 1
    assert test_phone.name == "iPhone 14"
    assert test_phone.price == 120000
    assert test_phone.quantity == 5
    assert test_phone.number_of_sim == 2


def test_phone_repr(test_phone):
    assert repr(test_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_str(test_phone):
    assert str(test_phone) == 'iPhone 14'


def test_phone_number_of_sim(test_phone):
    assert test_phone.number_of_sim == 2

    try:
        test_phone.number_of_sim = 0
    except ValueError:
        'Количество физических SIM-карт должно быть целым числом больше нуля.'
    test_phone.number_of_sim = 1
    assert test_phone.number_of_sim == 1
