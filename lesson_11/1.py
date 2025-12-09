"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран:
        <Бренд-Модель> - Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:
    """Класс для представления телефона.

    :param brand(str): Брэнд телефона
    :param model(str): Модель телефона
    :param issue_year(int): Год выпуска телефона
    """

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name: str):
        """Выводит сообщение о входящем звонке

        :param name (str): Имя звонящего.
        """
        print(f"<{self.brand}-{self.model}> — Звонит {name}")

    def get_info(self) -> tuple:
        """Возвращает информацию об устройстве
        Returns:
            tuple: (brand, model, issue_year)
        """
        return (self.brand, self.model, self.issue_year)

    def __str__(self) -> str:
        """Выводит на экран информацию о телефоне
        Returns:
            str: brand, model, issue_year
        """

        return (
            f"Брэнд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}"
        )


iphone = Phone("Apple", "iphone15", 2024)

iphone.receive_call("Сергей")
print(iphone)
print(iphone.get_info())
