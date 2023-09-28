from src.item import Item


class Phone(Item):
    def __init__(self, name:str, price:int, quantity:int, number_of_sim:int):
        """
        Создание экземпляров подкласса Phone на основе класса Item
        :param name: одель телефона
        :param price: цена за одну единицу
        :param quantity: количество единиц
        :param number_of_sim: количество встроенных симкарт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self) -> str:
        """
        Отладочная информация для разработчиков
        :return: строка с информацией
        """
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self) -> str:
        """
        Информация об экземпляре класса Phone для пользователей
        :return: строка с информацией
        """
        return f'{self.name}'

    @property
    def number_of_sim(self) -> int:
        """
        Геттер приватного атрибута __number_of_sim
        :return: количество встроенных симкарт
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """
        Сеттер приватного атрибута __number_of_sim
        :param value: значение количества встроенных симкарт
        :return: Сооветствие требованию наличия необходимого количества симкарт в числовом значении
        """
        if value <= 0 and isinstance(value, int):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = value

