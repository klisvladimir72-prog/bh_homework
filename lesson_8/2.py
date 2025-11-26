"""
Написать функцию которая принимает 2 стороны прямоугольника
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

"""


def calc_rectangle(length: float, width: float, perimeter=False) -> float:
    """Принимает 2 стороны прямоугольника
    perimeter = True => возвращает периметр, иначе — площадь
    """

    if perimeter:
        return (length + width) * 2

    return width * length


print(calc_rectangle(3, 4))
print(calc_rectangle(3, 4, True))
