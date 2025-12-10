"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Декущего ля года
  издания дополнительно проверить на валидность (> 0, <= тгода).

Аксессоры реализоваться через property.
"""

import datetime
from typing import Optional
from pprint import pprint


class BookCard:
    """
    Класс для представления карточки книги

      :param author: Имя автора
      :type author: str
      :param title: Название книги
      :type title: str
      :param year: Год издания книги
      :type year: int
    """

    def __init__(self, author: str, title: str, year: int):
        self.author = author
        self.title = title
        self.year = year

    @property
    def author(self) -> str:
        return self._author.strip().title()

    @author.setter
    def author(self, value: str):
        if not isinstance(value, str):
            raise ValueError(f"Должна быть строка, передано - {type(value)}")
        self._author = value.strip().title()

    @property
    def title(self) -> str:
        return self._title.strip().capitalize()

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str):
            raise ValueError(f"Должна быть строка, передано - {type(value)}")
        self._title = value.strip().capitalize()

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int):
        if not isinstance(value, int):
            raise ValueError(f"Должно быть целое число, передано - {type(value)}")

        current_year = datetime.datetime.now().year
        if current_year < value <= 0:
            raise ValueError(f"Год {value} должен быть реальным.")

        self._year = value

    def __eq__(self, other) -> bool:
        if not isinstance(other, BookCard):
            raise NotImplemented
        return self.year == other.year

    def __ne__(self, other) -> bool:
        if not isinstance(other, BookCard):
            raise NotImplemented
        return self.year != other.year

    def __lt__(self, other) -> bool:
        if not isinstance(other, BookCard):
            raise NotImplemented
        return self.year < other.year

    def __le__(self, other) -> bool:
        if not isinstance(other, BookCard):
            raise NotImplemented
        return self.year <= other.year

    def __gt__(self, other) -> bool:
        if not isinstance(other, BookCard):
            raise NotImplemented
        return self.year > other.year

    def __ge__(self, other) -> bool:
        if not isinstance(other, BookCard):
            raise NotImplemented
        return self.year >= other.year

    def __repr__(self) -> str:
        return f"BookCard(author='{self.author}', title='{self.title}', year='{self.year}')"


books = [
    BookCard("Толстой", "Война и мир", 1869),
    BookCard("Достоевский", "Преступление и наказание", 1866),
    BookCard("Оруэлл", "1984", 1949),
    BookCard("Харпер Ли", "Убить пересмешника", 1960),
]

pprint(sorted(books))
print()
pprint(sorted(books, reverse=True))
