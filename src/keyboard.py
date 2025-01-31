from src.item import Item


class LanguageMixin:
    """
    Language switcher mixin
    """

    def change_lang(self):
        """
        Method for switching keyboard input language between EN and RU
        :return: switching language from EN to RU
        """
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int):
        """
        Instantiating the Keyboard classInstantiating the Keyboard class
        :param name: the parameter is pulled from the parent Item class
        :param price: the parameter is pulled from the parent Item class
        :param quantity: the parameter is pulled from the parent Item class
        :param language: Keyboard class parameter with default value 'EN'
        """
        super().__init__(name, price, quantity)
        self._language = 'EN'

    @property
    def language(self):
        """
        Getter of language private atribute
        :return: keyboard layout language
        """
        return self._language
