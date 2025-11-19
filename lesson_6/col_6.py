'''
Запросить 3 раза строку из нескольких чисел через пробел
    - вывести все уникальные числа по возрастанию
    - вывести числа которые есть в каждой строке
    -* вывести числа которые есть только в одной из трех строк
    
    выполнить без циклов и условий
    
    пример:
    >>> 1 2 11 22
    >>> 1 2 22 33
    >>> 1 2 33 44


    1) 1 2 11 22 33 44
    2) 1 2
    3) 11 44
    
'''



line1 = input("Введите первую строку чисел: ")
line2 = input("Введите вторую строку чисел: ")
line3 = input("Введите третью строку чисел: ")


set1 = set(map(int, line1.split()))
set2 = set(map(int, line2.split()))
set3 = set(map(int, line3.split()))


all_unique = sorted(set1 | set2 | set3)


in_all = sorted(set1 & set2 & set3)


only_in_one = (
    (set1 - set2 - set3) |  
    (set2 - set1 - set3) |  
    (set3 - set1 - set2)    
)
only_in_one_sorted = sorted(only_in_one)


print("\nРезультаты:")
print("1)", " ".join(map(str, all_unique)))
print("2)", " ".join(map(str, in_all)))
print("3)", " ".join(map(str, only_in_one_sorted)))
