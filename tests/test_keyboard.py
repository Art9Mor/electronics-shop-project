import pytest

from src.keyboard import Keyboard


@pytest.fixture
def test_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_init(test_keyboard):
    assert len(test_keyboard.all) == 1
    assert test_keyboard.name == 'Dark Project KD87A'
    assert test_keyboard.price == 9600
    assert test_keyboard.quantity == 5
    assert test_keyboard.language == "EN"


def testng_language_changer(test_keyboard):
    test_keyboard.change_lang()
    assert test_keyboard.language == 'RU'
    test_keyboard.change_lang()
    assert test_keyboard.language == 'EN'
    try:
        test_keyboard.language = 'CH'
    except AttributeError:
        "property 'language' of 'Keyboard' object has no setter"


def test_keyboard_str(test_keyboard):
    assert str(test_keyboard) == 'Dark Project KD87A'
    assert str(test_keyboard.language) == 'EN'


def test_keyboard_repr(test_keyboard):
    assert repr(test_keyboard) == "Keyboard('Dark Project KD87A', 9600, 5)"
