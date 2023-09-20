"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item():
    return Item("Монитор Samsung", 17000, 3)


def test_item_init(test_item):
    assert len(test_item.all) == 1
    assert test_item.pay_rate == 1
    assert test_item.name == 'Монитор Samsung'
    assert test_item.price == 17000
    assert test_item.quantity == 3


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 51000


def test_apply_discount(test_item):
    test_item.apply_discount()
    assert test_item.price == 13600.0


def test_name(test_item):
    test_item.name = 'Монитор Samsung'
    assert test_item.name == 'Монитор Sa'
    test_item.name = 'Samsung'
    assert test_item.name == 'Samsung'


def test_string_to_number():
    assert Item.string_to_number('13') == 13
    assert Item.string_to_number('666.999') == 666
    assert Item.string_to_number('To.Cold') is None
    assert Item.string_to_number('To Old') is None


def test_repr(test_item):
    assert repr(test_item) == "Item('Монитор Samsung', 17000, 3)"

def test_instantiate_from_csv():
    print(Item.instantiate_from_csv('src/items.csv'))
    print(Item.all)