"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):
    """
        Функция принимает неограниченное количество позиционных и именованных аргументов.
    Проверяет типы и возвращает словарь с суммой позиционных аргументов и
    максимальной длиной ключа именованных аргументов.

    Raises:
        TypeError: "Все позиционные аргументы должны быть целыми"
        TypeError: "Все аргументы - ключевые слова должны быть строками"

    Returns:
    {
        "args_sum": 13,
        "kwargs_max_len": 7
    }
    """
    args_sum = 0
    kwargs_max_len = 0

    if args:
        try:
            for arg in args:
                if not isinstance(arg, int) or isinstance(arg, bool):
                    raise TypeError(
                        "Все позиционные аргументы должны быть целыми")
            args_sum = sum(args)
        except TypeError:
            raise

    if kwargs:
        try:
            for key in kwargs.keys():
                if not isinstance(key, str):
                    raise TypeError(
                        "Все аргументы - ключевые слова должны быть строками")
            kwargs_max_len = max(len(key) for key in kwargs.keys())
        except TypeError:
            raise

    return {
        "args_sum": args_sum,
        "kwargs_max_len": kwargs_max_len
    }



result = dict_from_args(1, 2, 3, 4, name="Alice", age=30, city="Moscow")
result2 = dict_from_args(1, 2, 3, 4, **{2:"Alice", 4:30, 3:"Moscow"}) # поясните эту строку 
print(result) 
print(result2) 


#  всегда падает ошибка еще при распаковке 
# а при вводе  dict_from_args(1, 2, 3, 4, 2:"Alice", 4:30, 3:"Moscow")=> пишет ошибку синтаксиса
# как быть в таких случаях и как это можно обойти если я хочу задать все-таки в других примерах числовые ключи 
