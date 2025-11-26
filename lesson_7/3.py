"""
Запросить любое число. Заменить каждую цифру этого числа буквой,
у которой номер в алфавите равен этой цифре.
Алфавит считаем от 0. a-0, b-1, c-3 и т.д.
Например: 13520 -> bdfca.
"""

letter_digit_dict = {
    0: "а",
    1: "б",
    2: "в",
    3: "г",
    4: "д",
    5: "е",
    6: "ж",
    7: "з",
    8: "и",
    9: "й",
}

while True:
    user_number = input(f"Введите любое число: ").strip()

    if user_number.isdigit():
        code = ""
        for num in user_number:
            code += letter_digit_dict.get(int(num))
        print(code)
        break

    print(f"❌ Введите корректное число!")
