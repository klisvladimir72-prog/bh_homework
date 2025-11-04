"""
Программа должна запросить у пользователя имя и подставить его в шаблон в место <имя>.
Шаблон менять нельзя.
Шаблон - "Юзер с именем <имя> заходил на сайт в 15:00"
Вывести результат на экран.

"""

from datetime import datetime

userName = input("Введите имя: ").strip().capitalize()
entryDate = datetime.now().strftime("%H:%M")

templateEntryUser = "Юзер с именем {} заходил на сайт в {}"

print(templateEntryUser.format(userName, entryDate))
