"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""
import re

users = [
    {"name": "Alice", "login": "alice", "password": "1234"},
    {"name": "Bob", "login": "bob", "password": "strongpass"},
    {"name": "Charlie", "login": "charlie", "password": "123"},
    {"name": "David", "login": "david", "password": "password123"},
    {"name": "Eve", "login": "eve@login", "password": "secure"},
]

short_password_users = list(
    filter(lambda user: len(user["password"]) < 5, users))

print("Пользователи с коротким паролем:")
for user in short_password_users:
    print(user)



invalid_login_users = list(
    filter(lambda user: not re.fullmatch(r"[a-zA-Z0-9_]+", user["login"]), users))

for user in invalid_login_users:
    print(f'Уважаемый {user["name"]}, ваш логин {user["login"]} не является корректным.')
