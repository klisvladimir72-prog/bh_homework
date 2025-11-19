'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))


if a >= b and a >= c:
    max_number = a
elif b >= a and b >= c:
    max_number = b
else:
    max_number = c


print(f"Наибольшее число: {max_number}")
