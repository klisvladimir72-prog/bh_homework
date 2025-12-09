"""
*
класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты(свойства):
    - value - текущее значение счетчика
    ...

Определить методы:
    - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
    - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
    - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
    - reset, сбрасывает значение счетчика на стартовое
    - метод __iter__
    - метод __next__

    ** - stat, возвращает среднее количество изменений счетчика в секунду

"""

import time
from typing import Union


class Counter:
    """Класс для целочисленного счетчика, который может увеличивать или уменьшать
    значение в заданном диапазоне (опционально).

    :param start(int) - начальное значение счетчика (default = 0)
    :param min_value(int) - минимальное значение (if None , без ограничения)
    :param max_value(int) - максимальное значение (if None, без ограничения)
    """

    def __init__(self, start: int = 0, min_value: int = None, max_value: int = None):
        self.value = start
        self.min_value = min_value
        self.max_value = max_value

        self._start = start
        self._changes_count = 0
        self._start_time = time.time()

    def _update_stats(self):
        """Считает количество count"""
        self._changes_count += 1

    def _is_range(self, value: int):
        """Задает число count в пределах заданного диапазона.

        :param value(str) - число для проверки.
        """

        if self.min_value is not None and value < self.min_value:
            return self.min_value
        if self.max_value is not None and value > self.max_value:
            return self.max_value
        return value

    def increase(self, num: int = 1):
        """Увеличивает счетчик на num (по умолчанию = 1).

        :param num (int, optional): Шаг увеличения Defaults to 1.
        """

        new_value = self._is_range(self.value + num)
        if new_value != self.value:
            self.value = new_value
            self._update_stats()

    def decrease(self, num: int = 1):
        """
        Уменьшает счетчик на num (default = 1)

        :param num: Шаг уменьшения (default = 1)
        :type num: int
        """

        new_value = self._is_range(self.value - num)
        if new_value != self.value:
            self.value = new_value
            self._update_stats()

    def reset(self):
        """
        Сбрасывает счетчик на начальное значение.
        """

        self.value = self._start
        self._changes_count = 0
        self._start_time = time.time()

    def __iter__(self):
        """
        Делает объект итерируемым.
        """
        return self

    def __next__(self):
        """Увеличивает счетчик на 1 и возвращает новое значение.
        При достижении max_value останавливается.
        """

        if self.max_value is not None and self.value >= self.max_value:
            raise StopIteration
        self.increase()

        return self.value

    def stat(self) -> str:
        """
        Docstring для stat

        :return: Среднее количество изменений в секунду
        :rtype: str(:.2f)
        """

        elapsed_time = time.time() - self._start_time
        if elapsed_time == 0:
            return 0
        return f"{(self._changes_count / elapsed_time):.2f}"

    def __repr__(self) -> str:
        return (
            f"Counter(value={self.value}, min={self.min_value}, max={self.max_value})"
        )


counter = Counter(2, 0, 8)
print(counter)
counter.increase(2)
print(counter.value)
counter.decrease(5)
print(counter.value)
print(f"Среднее количество изменений в секунду: {counter.stat()}")

print(next(counter))
print(next(counter))

for val in counter:
    print(val)
