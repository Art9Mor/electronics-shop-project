from src.item import Item


class LanguageMixin:

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'


class Keyboard(Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.language = 'EN'


@property
def language(self):
    return self.language


@language.setter
def language(self, lang):
    if lang not in ('EN', 'RU'):
        raise AttributeError("property 'language' of 'Keyboard' object has no setter")
    self.language = lang
