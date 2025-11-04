"""
запросить у пользователя два числа
вернуть значение где первое число возведено в степень второго числа

"""

valuesUser = []
userRequests = ["Введите первое число: ", "Введите второе число: "]

for request in userRequests:
    valuesUser.append(int(input(request)))

print(f"{valuesUser[0]} в степени {valuesUser[1]} = {valuesUser[0] ** valuesUser[1]}")
