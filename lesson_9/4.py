'''
Дан список [1,2,3,4,5,6,7,8,9]. Создать 3 копии этого списка 
и с каждой выполнить след действия:
    - возвести каждый элемент во 2ю степень
    - прибавить 3 к каждому элементу значение которого является четным 
    - элементы значения которого является 
            четными - умножить на 2 
            нечетным - умножить на 3

Использовать map и lambda.
'''

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list1 = original_list[:]
list2 = original_list[:]
list3 = original_list[:]

result1 = list(map(lambda x: x ** 2, list1))

result2 = list(map(lambda x: x + 3 if x % 2 == 0 else x, list2))

result3 = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, list3))

print("Оригинальный список:", original_list)
print("1. Каждый элемент в степени 2:", result1)
print("2. Чётные + 3:", result2)
print("3. Чётные * 2, нечётные * 3:", result3)
