"""
Дан произвольный список. Вывести на экран в обратном порядке.
Задачу решить 2мя способами.
"""

test_list = [1, 2, 3, 45, "hello"]

print(test_list[::-1])

print_list = test_list[:]
print_list.reverse()

print(print_list)
