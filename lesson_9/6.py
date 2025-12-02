"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""

observations = {"day1": 18, "day2": 22, "day3": 7, "day4": 11, "day5": 14}

sorted_increase = dict(sorted(observations.items(), key=lambda item: item[1]))
print("По возрастанию:", sorted_increase)

sorted_decrease = dict(
    sorted(observations.items(), key=lambda item: item[1], reverse=True))
print("По убыванию:", sorted_decrease)
