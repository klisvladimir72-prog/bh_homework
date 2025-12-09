"""
1.Открыть и обработать файл students_grades.txt.
2.Собрать все данные в словарь ниже приведенного формата.
3.Записать в файл "excellent_students.txt" учеников из каждого класса с наибольшим балом.
{
    "9A":[
        {'fio':'fio',
         'objects':{
            'mathematics':[4, 9, 7],
            'physics':[8, 9, 8, 6],
            ...:...
            }
        },
        ...
    ],
    "9Б":[
        ...
    ]
}

"""

# пока неправильно не смотрите (расчет оценок хромает, не успеваю просмотреть косяки)
import re
from pprint import pprint

# парсим оценки по предметам


def parse_grades(grades_str: str):
    pattern = r"([^,]+?)\s*\((.*?)\)"
    matches = re.findall(pattern, grades_str)

    result = {}
    for subj_part, grades_part in matches:
        subj_name = subj_part.strip()
        try:
            grades_list = [int(x.strip()) for x in grades_part.split(",")]
        except ValueError:
            continue
        result[subj_name] = grades_list

    return result


# разбираем файл
def read_file(file_name):
    data = {}

    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            parts = line.split(", ", 2)

            fio = parts[0]
            class_name = parts[1]
            subj_grades = parts[2]

            subjects = parse_grades(subj_grades)

            student = {"fio": fio, "subjects": subjects}

            if class_name not in data:
                data[class_name] = []
            data[class_name].append(student)

    return data


def find_best_student_in_class(student_list):
    best_student = None
    highest_avg = -1

    for student in student_list:
        avg = calculate_average(student)
        if avg > highest_avg:
            highest_avg = avg
            best_student = student

    return best_student, highest_avg if best_student else 0.0


def calculate_average(student):
    total_grades = 0
    count = 0
    for subject_grades in student["subjects"].values():
        total_grades += sum(subject_grades)
        count += len(subject_grades)

    if count == 0:
        return 0.0

    return round(total_grades / count, 2)


def save_excellent_student(data, output_file_name):
    with open(output_file_name, "w", encoding="utf-8") as f:
        for class_name, students in data.items():
            best, highest_avg = find_best_student_in_class(students)
            if best:
                f.write(
                    f"Класс - {class_name}:\n  - ФИО - {best['fio']}, средний бал - {highest_avg} \n"
                )


file_name = "students_grades.txt"
output_file = "excellent_students_my.txt"


data = read_file(file_name)
save_excellent_student(data, output_file)

pprint(data)
