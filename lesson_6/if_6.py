"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""

a1 = 3.5
a2 = 4.0
a3 = 7.2
a4 = 9.1


all_float = (
    isinstance(a1, float) and
    isinstance(a2, float) and
    isinstance(a3, float) and
    isinstance(a4, float)
)


one_is_string = (
    isinstance(a1, str) or
    isinstance(a2, str) or
    isinstance(a3, str) or
    isinstance(a4, str)
)



pair_a1_a3 = isinstance(a1, int) and isinstance(a3, int)
pair_a2_a4 = isinstance(a2, int) and isinstance(a4, int)
pair_a3_a4 = isinstance(a3, int) and isinstance(a4, int)

one_pair_int = pair_a1_a3 or pair_a2_a4 or pair_a3_a4


print("1)", all_float)
print("2)", one_is_string)
print("3)", one_pair_int)
