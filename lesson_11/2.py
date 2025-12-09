"""
Создать класс Student.


Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""

from typing import List
from pprint import pprint


class Student:
    """Класс создания студента.

    :param surname(str) - фамилия
    :param name(str) - имя
    :param group(int) - номер группы
    :param grads(list) - список оценок(может быть пустой)
    """

    def __init__(self, surname: str, name: str, group: int, grads: List[int] = None):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grads if grads is not None else []

    def add_grade(self, *grades: int):
        """Добавляет одну или несколько оценок в список.
        Проверяет что каждая оценка от 0 до 10.

        :param grades(int): одна или несколько оценок.
        """
        for grade in grades:
            if not 0 <= grade <= 10:
                raise ValueError(f"Оценка {grade} вне диапазона реальных оценок.")
            self.grads.append(grade)

    def average_grade(self) -> float:
        """Высчитывает средний бал студента.
            Если список пуст возвращает 0.

        :return float: средний бал
        """
        if not self.grads:
            return 0.0
        return sum(self.grads) / len(self.grads)

    def __str__(self) -> str:
        return f"{self.surname} {self.name}, группа {self.group}, оценки: {self.grads}, средний балл: {self.average_grade():.2f}"

    def __repr__(self) -> str:
        return f"Student(surname='{self.surname}', name='{self.name}', group={self.group}, grads={self.grads})"

    def __eq__(self, other: Student) -> bool:
        """Равен ли средний бал с другим студентом.

        :param other(Student): Объект класса Student

        :return bool: результат сравнения
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __ne__(self, other: Student) -> bool:
        """Проверяет не равны ли средние балы студентов.

        :param other(Student): Объект класса Student

        :return bool: результат сравнения
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() != other.average_grade()

    def __lt__(self, other: Student) -> bool:
        """Меньше ли средний бал с другим студентом.

        :param other(Student): Объект класса Student

        :return bool: результат сравнения
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __gt__(self, other: Student) -> bool:
        """Больше ли средний бал с другим студентом.

        :param other(Student): Объект класса Student

        :return bool: результат сравнения
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __le__(self, other: Student) -> bool:
        """Меньше или равен средний бал с другим студентом.

        :param other(Student): Объект класса Student

        :return bool: результат сравнения
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other: Student) -> bool:
        """Больше или равен средний бал с другим студентом.

        :param other(Student): Объект класса Student

        :return bool: результат сравнения
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() >= other.average_grade()


students = [
    Student("Иванов", "Иван", 1, [8, 9, 7]),
    Student("Петров", "Петр", 2, [10, 10, 9, 9]),
    Student("Сидоров", "Алексей", 1, [6, 7, 5]),
    Student("Кузнецов", "Дмитрий", 3, [8, 8, 8, 9]),
    Student("Смирнов", "Андрей", 2, [9, 10, 10, 9, 8]),
]

pprint(list(sorted(students)))
print()
pprint(list(sorted(students, reverse=True)))
print("\n>8")
for s in sorted(students, reverse=True):
    if s.average_grade() > 8:
        print(s)
