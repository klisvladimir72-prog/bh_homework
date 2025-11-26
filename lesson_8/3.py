"""
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

"""


def get_factorial(n: int) -> int:
    """_summary_
    Вычисляет  факториал переданного в нее числа
    Args:
        n (int): положительное число для расчета факториала

    Returns:
        int: факториал числа "n"
    """

    if n < 0:
        raise ValueError("Факториал рассчитывается только для положительных чисел!")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


print(get_factorial(5))
print(get_factorial(0))
print(get_factorial(1))
print(get_factorial(-1))
