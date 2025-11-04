"""
запросить у пользователя три значения присвоить их в разные переменные
и  выведите одной функцией print в след вариантах:
        - одна строку через пробел
        - одну строку через " : "
        - три строки начиная с дефиса
"""

valuesUser = []
userRequests = [
    "Введите ваше имя: ",
    "Введите ваше отчество: ",
    "Введите свой возраст: ",
]

for request in userRequests:
    valuesUser.append(input(request))

formatDash = "\n".join(["-" + "{}"] * len(valuesUser))

print(*valuesUser)
print(*valuesUser, sep=" : ")
print(formatDash.format(*valuesUser))
