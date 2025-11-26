# '''

# *
# В структуре данных из 5 урока задание №2 каждому сотруднику
# добавить к параметру "навык" параметр "мастерство" измеряемый от 0 до 100
#
# Написать программу которая анализирует всю структуру данных и выводит сотрудников
# с наибольшим параметром "мастерство" для каждого существующего навыка.
# Пример вывода:
#     1. Python - Иванов - 98
#     2. JS - Петров  - 74
#     3. Базы данных - Николаев - 87
#     ...
#
#
# ** Пример вывода (перед выводам отсортировать по убыванию "мастерства"):
#
#     --------------------------------------------------
#     | № |   Навык     |       ФИО       | Мастерство |
#     ==================================================
#     | 1 | Python      | Иванов Н.С.     |     98     |
#     | 2 | JS          | Петров В.В.     |     87     |
#     | 3 | Базы данных | Николаев Е.Н.   |     74     |
#     ...
# '''

from pprint import pprint

employees = [
    {
        "surname": "Иванов",
        "name": "Иван",
        "last_name": "Иванович",
        "post": "Python-разработчик",
        "birth_year": 1990,
        "skills": [
            {"name": "Python", "mastery": 90},
            {"name": "Django", "mastery": 85},
            {"name": "Docker", "mastery": 80},
            {"name": "Git", "mastery": 75},
        ],
        "childrens": [
            {"name": "Анна", "birth_year": 2010},
            {"name": "Михаил", "birth_year": 2018},
        ],
    },
    {
        "surname": "Петрова",
        "name": "Мария",
        "last_name": "Сергеевна",
        "post": "HR-менеджер",
        "birth_year": 1985,
        "skills": [
            {"name": "Рекрутинг", "mastery": 95},
            {"name": "Кадровый учёт", "mastery": 88},
            {"name": "Тренинги", "mastery": 82},
        ],
        "childrens": [{"name": "Елена", "birth_year": 2010}],
    },
    {
        "surname": "Сидоров",
        "name": "Алексей",
        "last_name": "Петрович",
        "post": "DevOps-инженер",
        "birth_year": 1992,
        "skills": [
            {"name": "Linux", "mastery": 92},
            {"name": "Ansible", "mastery": 85},
            {"name": "Kubernetes", "mastery": 88},
            {"name": "CI/CD", "mastery": 87},
        ],
        "childrens": [],
    },
]

skill_max = {}

for employee in employees:
    for skill in employee["skills"]:
        skill_name = skill["name"]
        mastery = skill["mastery"]

        if skill_name not in skill_max or mastery > skill_max[skill_name]["mastery"]:
            skill_max[skill_name] = {
                "mastery": mastery,
                "employee": f"{employee['surname']} {employee["name"][0]}.{employee['last_name'][0]}.",
            }

sort_skills = sorted(skill_max.items(), key=lambda x: x[1]["mastery"], reverse=True)

len_col_number = len(str(len(skill_max))) + 2
len_col_skill = max(len(key) for key in skill_max.keys()) + 4
len_col_name = max(len(value["employee"]) for value in skill_max.values()) + 4
len_col_mastery = len("Мастерство") + 4

len_row = len_col_number + len_col_skill + len_col_name + len_col_mastery

print(f"{"-" * len_row}")
print(
    f"|{'№':^{len_col_number}}|{'Навык':^{len_col_skill}}|{'ФИО':^{len_col_name}}|{"Мастерство":^{len_col_mastery}}|"
)
print(f"{"=" * len_row}")

for i, (key, value) in enumerate(sort_skills, 1):
    fio = value["employee"]
    mastery = value["mastery"]

    print(
        f"|{i:^{len_col_number}}|{key:<{len_col_skill}}|{fio:<{len_col_name}}|{mastery:^{len_col_mastery}}|"
    )

print(f"{"-" * len_row}")
