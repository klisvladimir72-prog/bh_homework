
"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial():
    """
    Генератор факториала возвращает новое значение по возрастанию (1!->2!->3!....).
    """

    n = 0
    result = 1

    while True:
        yield result
        n += 1
        result *= n


factorial_gen = factorial()

print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
