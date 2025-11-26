"""
Запросить высоту елочки - число от 3 до 20.
Напечатать на экране елочку где ее высота равна числу строк.
Пример елочки из 4 строк:
   *
  ***
 *****
*******

* - елочка со снегом
"""

import random
from colorama import Fore, Style


while True:
    try:
        height = int(input("Введите высоту елки (от 3 до 20): "))

        if 3 <= height <= 20:
            break

        print("❌ Высота должна быть от 3 до 20!")

    except Exception as e:
        match type(e).__name__:
            case "ValueError":
                print("❌ Значение должно быть числом от 3 до 20!")
            case _:
                print(f"❌ Ошибка: {type(e).__name__} - {str(e)}")


for i in range(1, height * 2, 2):
    line = list(f"{'∧' * (i):^{height*2}}")
    spaces = [ind for ind, char in enumerate(line) if char == " "]

    count_spaces = random.randint(0, len(spaces) // 4)
    choice_ind_of_spaces = random.sample(spaces, count_spaces)

    for i in choice_ind_of_spaces:
        line[i] = "⨳"

    final_line = "".join(line)

    color_line = final_line.replace("∧", Fore.GREEN + "∧" + Style.RESET_ALL).replace(
        "⨳", Fore.WHITE + "⨳" + Style.RESET_ALL
    )
    print(color_line)
