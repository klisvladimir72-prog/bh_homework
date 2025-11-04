"""
Программа должна запросить несколько цифр через пробел
    - выдать их общую сумму
    - выдать максимальную цифру
    - выдать среднее арифметическое

"""

while True:
    userRequest = input("Введите три числа через пробел: ").split(" ")
    if len(userRequest) != 3:
        print("Количество чисел должно быть 3!")
        continue

    try:
        userRequest = list([int(number) for number in userRequest])
        break
    except ValueError:
        print("Значение должно быть числом и без знаков!")

print(f"Сумма: {sum(userRequest)}")
print(f"Максимальное значение: {max(userRequest)}")
print(f"Среднее арифметическое: {sum(userRequest) / len(userRequest)}")
