"""
Запросить у пользователя год рождения и в соответствии с его возрастом 
охарактеризовать пользователя - 
ребенок, подросток, юноша, в расцвете сил, пожилой, старик.
"""
from datetime import datetime

current_year = datetime.now().year


birth_year = int(input("Введите ваш год рождения: "))

age = current_year - birth_year

categories = {
    (0, 12): "ребёнок",
    (13, 17): "подросток",
    (18, 24): "юноша",
    (25, 59): "в расцвете сил",
    (60, 74): "пожилой",
    (75, 150): "старик"
}


match age:
    case n if 0 <= n <= 12:
        description = "ребёнок"
    case n if 13 <= n <= 17:
        description = "подросток"
    case n if 18 <= n <= 24:
        description = "юноша"
    case n if 25 <= n <= 59:
        description = "в расцвете сил"
    case n if 60 <= n <= 74:
        description = "пожилой"
    case n if 75 <= n <= 150:
        description = "старик"
    case _:  
        description = "возраст вне допустимого диапазона"


print(f"Возраст: {age} лет — {description}")
