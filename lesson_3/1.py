"""
запросить у пользователя три значения присвоить их в разные переменные
и  выведите одной функцией print в след вариантах:
        - одна строку через пробел
        - одну строку через " : "
        - три строки начиная с дефиса
"""

values_user = []
user_requests = [
    "Введите ваше имя: ",
    "Введите ваше отчество: ",
    "Введите свой возраст: ",
]

for request in user_requests:
    values_user.append(input(request))

formatDash = "\n".join(["-{}"] * len(values_user))

print(*values_user)
print(*values_user, sep=" : ")
print(formatDash.format(*values_user))
