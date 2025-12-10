"""
Описать абстрактный класс Animal у которого:

- атрибут name - кличка (тип str)
- магический метод __init__, который принимает аргумент name
- абстрактный метод says, который не принимает аргументов

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
says таким образом, чтобы он возвращал строку вида:

- "{кличка} - кошка. Говорит МЯУ!" для класса Cat
- "{кличка} - собака. Говорит ГАВ!" для класса Dog
- "{кличка} - корова. Говорит МУ!" для класса Cow
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Абстрактный метод представляющий животное

    :param name: Кличка животного
    :type name: str
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def says():
        """
        Абстрактный метод для звуков животного
        """
        pass


class Cat(Animal):
    """
    :return голос кота
    """

    def says(self):
        return f"{self.name} - говорит МЯУ!"


class Dog(Animal):
    """
    :return голос собаки
    """

    def says(self):
        return f"{self.name} - говорит ГАВ!"


class Cow(Animal):
    """
    :return голос коровы
    """

    def says(self):
        return f"{self.name} - говорит МУУ!"


animals = [Cat("Мурка"), Dog("Шарик"), Cow("Бурёнка")]


for animal in animals:
    print(animal.says())
