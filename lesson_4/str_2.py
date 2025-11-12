"""
Программа должна запросить несколько цифр через пробел
    - выдать их общую сумму
    - выдать максимальную цифру
    - выдать среднее арифметическое

"""

while True:
    user_request = input("Введите три числа через пробел: ").split(" ")
    if len(user_request) != 3:
        print("Количество чисел должно быть 3!")
        continue

    try:
        user_request = list([int(number) for number in user_request])
        break
    except ValueError:
        print("Значение должно быть числом и без знаков!")

print(f"Сумма: {sum(user_request)}")
print(f"Максимальное значение: {max(user_request)}")
print(f"Среднее арифметическое: {sum(user_request) / len(user_request)}")
