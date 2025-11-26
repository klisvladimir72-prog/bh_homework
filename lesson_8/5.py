"""
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

"""

from pprint import pprint


def count_char(s: str) -> dict:
    """
    Принимает строку и возвращает словарь,
    где ключи — это символы строки, а значения — количество их вхождений.

    Args:
        s (str): строка, для которой считается количество символов

    Returns:
        dict: словарь вида {'символ': количество_вхождений}
    """
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


pprint(count_char("hello"))
pprint(count_char("абракадабра"))
pprint(count_char(""))
