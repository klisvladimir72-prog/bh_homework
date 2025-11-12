"""
Пользователь вводит 3 числа,
найти среднее арифметическое с точность 3 знака после запятой

"""

values_user = []
user_requests = [
    "Введите первое число: ",
    "Введите второе число: ",
    "Введите третье число: ",
]

for number in user_requests:
    while True:
        try:
            value = float(input(number))
            values_user.append(value)
            break
        except ValueError:
            print("Введите число!")

result = sum(values_user) / len(values_user)

print(f"Среднее арифметическое: {result:.3f}")
