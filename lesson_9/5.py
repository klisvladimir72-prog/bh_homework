'''
*
Написать рекурсивную функцию, которая принимает список 
и печатает каждых элемент на новой строке. 
Если элемент списка - список, то его элементы должны выводиться 
с отступом относительно родительского на 2 символа. 
Символ для отступа передать дополнительными необязательным параметром.

** написать такую же функцию но без рекурсии

Пример1: some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]
1
2
3
--4
----5
----6
--7
8
9

Пример2: some_list=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]
1
--2
------3
----4
5
------6
------7
8
--------9
--------10
----11
12




'''


def print_list_recursive(lst: list, depth: int = 0, indent_char: str = '-'):
    """
    Рекурсивно печатает элементы списка с отступами.
    Если элемент — список, то его элементы печатаются с отступом на 2 символа больше

    Args:
        lst (list): спсиок на печать (может быть вложенный).
        depth (int, optional): уровень вложенности списка. По умолчанию == 0.
        indent_char (str, optional): знак для отступов. По умолчанию '-'.
    """
    for item in lst:
        if isinstance(item, list):
            print_list_recursive(item, depth + 1, indent_char)
        else:
            print(f"{indent_char * 2 * depth}{item}")


some_list1 = [1, 2, 3, [4, [5, 6], 7], 8, 9]
print_list_recursive(some_list1)
print("="*20)
some_list2 = [1, [2, [[3], 4]], 5, [[[6, 7]]], 8, [[[[9, 10]], 11]], 12]
print_list_recursive(some_list2)

# Без рекурсии
print(f"{'#'*20}\n")


def print_list_iterative(lst: list, indent_char: str = '-'):
    """
    Итеративно печатает элементы списка с отступами.
    Использует стек для отслеживания вложенности.

    Args:
        lst (list): список на печать (может быть с разной вложенностью).
        indent_char (str, optional): элемент для отображения отступов вложенности.
    """

    stack = [(item, 0) for item in reversed(lst)]

    while stack:
        item, depth = stack.pop()

        if isinstance(item, list):
            for sub_item in reversed(item):
                stack.append((sub_item, depth + 1))
        else:
            print(f"{indent_char * 2 * depth}{item}")



some_list1 = [1, 2, 3, [4, [5, 6], 7], 8, 9]
print_list_iterative(some_list1)
print("="*20)
some_list2 = [1, [2, [[3], 4]], 5, [[[6, 7]]], 8, [[[[9, 10]], 11]], 12]
print_list_iterative(some_list2)

