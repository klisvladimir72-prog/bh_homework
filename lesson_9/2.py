'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''


def factorial(n: int) -> int:
    """
    Рекурсивно вычисляет факториал числа n.

    Args:
        n (int): Натуральное число или 0.

    Returns:
        int: Факториал числа n.

    Raises:
        ValueError: Если n < 0.
        TypeError: Если n не является целым числом.
    """
    if not isinstance(n, int):
        raise TypeError("Факториал определён только для целых чисел.")
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел.")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(7))
print(factorial(-3))
