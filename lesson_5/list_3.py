"""
Дан произвольный список из 5 элементов.
     - Поменять местами 1ый и последний элемент
     - удалить и вывести на печать третий элемент
"""

test_list = [1, 2, 5, 56, "45", True]

test_list[0], test_list[-1] = test_list[-1], test_list[0]

print(test_list)
print(test_list.pop(2))

print(test_list)

