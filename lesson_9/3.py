
'''
Написать рекурсивную функцию, которая принимает 2 аргумента 
(целые числа - a и b) и высчитывает суммы всех чисел от a до b (включительно). 
Пример: a = 3, b = 5 -> 12 (3+4+5)
Пример: a = 5, b = 9 -> 35 (5+6+7+8+9)"

'''


def sum_range(a, b):
    """
    Рекурсивно вычисляет сумму всех целых чисел от a до b включительно.

    Args:
        a (int): Начальное число диапазона.
        b (int): Конечное число диапазона.

    Returns:
        int: Сумма чисел от a до b.

    Raises:
        TypeError: Если a или b не являются целыми числами.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Аргументы должны быть целыми числами.")

    if a > b:
        return 0

    if a == b:
        return a

    return a + sum_range(a + 1, b)


print(sum_range(1, 5))
print(sum_range(5, 9))
print(sum_range(1, 1))
print(sum_range(0, 0))
