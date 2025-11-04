"""
запросить число и вывести на экран сколько номиналов в этом числе:
         - тысячи
         - сотни
         - десятки
         - единицы

пример: # знак >>> значит что ввели что-то через input
    >>> 21234
    тысяч - 21
    сотни - 2
    десятки - 3
    единицы - 4
"""

while True:
    number = input("Введите число для расчета: ")

    if not number:
        print("Для расчета введите число от 0 до 999999")
        continue

    try:
        number = float(number)
        if number <= 0 or number >= 1000000:
            print("Число должно быть > 0 и меньше 1 000 000")
            continue
        break
    except ValueError:
        print("Ошибка: Введенное значение должно быть числом без знаков и символов!")
        continue  # необязательно -- больше для читабельности

number = int(number)
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
units = number % 10

print(f"тысяч - {thousands}")
print(f"сотен - {hundreds}")
print(f"десятки - {tens}")
print(f"единицы - {units}")
