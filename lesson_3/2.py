"""
запросить у пользователя два числа
вернуть значение где первое число возведено в степень второго числа

"""

values_user = []
user_requests = ["Введите первое число: ", "Введите второе число: "]

for request in user_requests:
    values_user.append(int(input(request)))

print(
    f"{values_user[0]} в степени {values_user[1]} = {values_user[0] ** values_user[1]}"
)
