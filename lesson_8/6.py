"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента,
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""


def yes_or_no(lst: list) -> list | bool:
    """
    Принимает список целых чисел и возвращает список из 'Yes' или 'No':
    - 'Yes' — если число уже встречалось ранее в списке,
    - 'No' — если число встречается впервые.
    Если в списке есть нецелые числа, возвращает False.

    Args:
        lst (list): список целых чисел

    Returns:
        list: ['Yes'/'No'] или False, если в списке не все целые числа
    """
    for item in lst:
        if not isinstance(item, int) or isinstance(item, bool):
            return False

    seen = set()
    result = []
    for num in lst:
        if num in seen:
            result.append("Yes")
        else:
            result.append("No")
            seen.add(num)
    return result


print(yes_or_no([1, 2, 3, 1, 4]))
