"""
Запросить по очереди у пользователя 5 имен. Добавить все в список.
Отсортировать.
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
"""

import re

names = []

while len(names) < 5:
    name = input(f"Введите имя {len(names) + 1}: ").strip().capitalize()

    if not re.match(r"^[А-Яа-я]+$", name):
        print("Имя не должно быть пустым и должно состоять только из русских букв!")
        continue

    names.append(name)

names.sort()

print("Список имен по афавиту: ", names)

if "Вася" in names:
    print(True)
