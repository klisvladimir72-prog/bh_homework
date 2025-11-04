"""
Запросить количество секунд.
Вывести на экран время в формате ЧЧ:ММ:СС равное эти секундам.
Пример: 35457 -> 09:50:57
Сделать 2 варианта с форматной строкой и без.

"""

while True:
    seconds = input("Введите количество секунд: ")

    if not seconds:
        print("Значение не должно быть пустым!")
        continue
    try:
        seconds = int(seconds)

        break
    except ValueError:
        print("Значение должно быть числом!")

hours = seconds // 3600
minutes = (seconds % 3600) // 60
second = seconds % 60


print(f"С 1970 года прошло: {hours:02}:{minutes:02}:{second:02}")
print(
    "С 1970 года прошло: "
    + str(hours).zfill(2)
    + ":"
    + str(minutes).zfill(2)
    + ":"
    + str(second).zfill(2)
)
