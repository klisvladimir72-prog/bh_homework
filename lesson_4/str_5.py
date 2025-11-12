"""
Программа должна запросить у пользователя имя и подставить его в шаблон в место <имя>.
Шаблон менять нельзя.
Шаблон - "Юзер с именем <имя> заходил на сайт в 15:00"
Вывести результат на экран.

"""

from datetime import datetime

user_name = input("Введите имя: ").strip().capitalize()
entry_date = datetime.now().strftime("%H:%M")

template_entry_user = "Юзер с именем {} заходил на сайт в {}"

print(template_entry_user.format(user_name, entry_date))
