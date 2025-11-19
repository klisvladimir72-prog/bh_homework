"""
2. Создать структуру данных сотрудников фирмы с 
    тремя сотрудниками. каждый сотрудник должен иметь:
        ФИО, 
        должность, 
        год рождения, 
        список навыков, 
        список детей с их именем и годом рождения. 
    
    Запросить ФИО сотрудника и вывести по нему информацию.
    
    ** задать вопрос о желании добавить сотрудника,
        если ответ да - добавить сотрудника через несколько input
        (после добавления сотрудника вывести всю структуру консоль)

"""

from pprint import pprint
import re

employees = [
    {
        "surname": "Иванов",
        "name": "Иван",
        "last_name": "Иванович",
        "post": "Python-разработчик",
        "birth_year": 1990,
        "skills": ["Python", "Django", "Docker", "Git"],
        "childrens": [
            {"name": "Анна", "birth_year": 2010},
            {"name": "Михаил", "birth_year": 2018}
        ]
    },
    {
        "surname": "Петрова",
        "name": "Мария",
        "last_name": "Сергеевна",
        "post": "HR-менеджер",
        "birth_year": 1985,
        "skills": ["Рекрутинг", "Кадровый учёт", "Тренинги"],
        "childrens": [
            {"name": "Елена", "birth_year": 2010}
        ]
    },
    {
        "surname": "Сидоров",
        "name": "Алексей",
        "last_name": "Петрович",
        "post": "DevOps-инженер",
        "birth_year": 1992,
        "skills": ["Linux", "Ansible", "Kubernetes", "CI/CD"],
        "childrens": []
    }
]

# Подготовка к поиску
def get_search_value():
    search_elem = 'фамилию'

    while True:
        user_input = input(
            f"Введите {search_elem} для поиска сотрудника: ").strip().lower()

        if re.fullmatch(r'[а-яёa-z\s\-\/]+', user_input):
            return user_input

        if re.fullmatch(r'\d+', user_input):
            return int(user_input)

        print("""
❌ Ошибка: могут быть только буквы и '-', цифры, пробелы, дефисы, и слеш🙄
Попробуйте снова.""")


def search_in_item(val, search):
    if isinstance(val, int) and isinstance(search, int):
        return val == search
    elif isinstance(val, str) and isinstance(search, str):
        return search in val.lower()
    return False


def search_in_dict(employee, search):
    if isinstance(employee, dict):
        for value in employee.values():
            if search_in_dict(value, search):
                return True

    elif isinstance(employee, list):
        for item in employee:
            if search_in_dict(item, search):
                return True

    else:
        return search_in_item(employee, search)

    return False


def replay():
    while True:
        replay = input(
            f"Хотите возобновить поиск сотрудника? (y/n): ").strip().lower()
        if replay in ['yes', 'нуы', 'y', 'н']:
            return True
        elif replay in ['no', 'тщ', 'n', 'т']:
            print(f"Возвращайтесь еще👋")
            return False
        else:
            print("Введите (y/n)!")


# Запуск поиска
while True:
    search_item = get_search_value()

    search_results = [
        employee for employee in employees if search_in_dict(employee, search_item)]

    if search_results:
        pprint(search_results, sort_dicts=False)
    else:
        print(f"Сотрудника не найдено🤔")

    if not replay():
        break


# Добавление нового сотрудника
while True:
    add_agree = input(
        "Хотите добавить нового сотрудника? (y/n): ").strip().lower()

    if add_agree in ['yes', 'нуы', 'y', 'н']:
        print("\nВведите данные нового сотрудника:")

        surname = input("Фамилия: ").strip().title()
        while not surname or not re.fullmatch(r'[а-яёa-z-]+', surname, re.IGNORECASE):
            surname = input(
                "Введите корректную фамилию (только буквы и '-'): ").strip().title()

        name = input("Имя: ").strip().title()
        while not name or not re.fullmatch(r'[а-яёa-z-]+', name, re.IGNORECASE):
            name = input(
                "Введите корректное имя (только буквы и '-'): ").strip().title()

        last_name = input("Отчество: ").strip().title()
        while not last_name or not re.fullmatch(r'[а-яёa-z-]+', last_name, re.IGNORECASE):
            last_name = input(
                "Введите корректное отчество (только буквы и '-'): ").strip().title()

        post = input("Должность: ").strip().title()
        while not post:
            post = input("Должность обязательна: ").strip().title()

        # Год рождения
        while True:
            try:
                birth_year = int(input("Год рождения: "))
                if 1900 <= birth_year <= 2025:
                    break
                else:
                    print("Год должен быть реальным 😂")
            except ValueError:
                print("Введите целое число!")

        # Навыки
        skills_input = input("Навыки (через запятую): ").strip()
        skills = [s.strip().title()
                  for s in skills_input.split(",")] if skills_input else []

        # Дети
        childrens = []
        while True:
            has_children = input("Есть дети? (y/n): ").strip().lower()
            if has_children in ['no', 'тщ', 'n', 'т']:
                break
            elif has_children in ['yes', 'нуы', 'y', 'н']:
                child_name = input("Имя ребёнка: ").strip().title()
                while not child_name or not re.fullmatch(r'[а-яёa-z-]+', child_name, re.IGNORECASE):
                    child_name = input(
                        "Введите корректное имя ребёнка (только буквы и '-'): ").strip().title()

                while True:
                    try:
                        child_birth = int(input("Год рождения ребёнка: "))
                        if 1900 <= child_birth <= 2025 and child_birth <= birth_year - 14:
                            break
                        else:
                            print("Год рождения ребёнка должен быть реалистичным.")
                    except ValueError:
                        print("Введите целое число.")

                childrens.append(
                    {"name": child_name, "birth_year": child_birth})

                more = input(
                    "Добавить ещё одного ребёнка? (да/нет): ").strip().lower()
                if more not in ['yes', 'нуы', 'y', 'н']:
                    break
            else:
                print("Введите 'да' или 'нет'.")

        # Создаём нового сотрудника
        new_employee = {
            "surname": surname,
            "name": name,
            "last_name": last_name,
            "post": post,
            "birth_year": birth_year,
            "skills": skills,
            "childrens": childrens
        }

        employees.append(new_employee)
        print(f"\n✔ Сотрудник '{surname} {name}' успешно добавлен!")
        break

    elif add_agree in ['no', 'тщ', 'n', 'т']:
        print("Добавление отменено.")
        break
    else:
        print("Введите 'да' или 'нет'.")

# Вывод всей структуры
print("\nОбновлённая база всех сотрудников:")
pprint(employees, sort_dicts=False)
