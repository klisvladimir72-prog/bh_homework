"""
Пользователь вводит 3 числа,
найти среднее арифметическое с точность 3 знака после запятой

"""

valuesUser = []
userRequests = [
    "Введите первое число: ",
    "Введите второе число: ",
    "Введите третье число: ",
]

for number in userRequests:
    while True:
        try:
            value = float(input(number))
            valuesUser.append(value)
            break
        except ValueError:
            print("Введите число!")

result = sum(valuesUser) / len(valuesUser)

print(f"Среднее арифметическое: {result:.3f}")
