"""

Написать функцию, которая возвращает любое число в виде денежной величины
с разделителями групп разрядов в качестве пробела и валютой в конце.
Денежная величина всегда должна содержать количество копеек в виде дух
знаков после точки, даже если исходное число целое.
*Нельзя использовать форматную строку.
Например: 1234567 -> "1 234 567.00 руб."

с помощью try перехватить возможные ошибки.
"""

# def format_in_monetary_rub(price: float) -> str:
#     """_summary_
#         возвращает любое число в виде денежной величины
#         с разделителями групп разрядов в качестве пробела и валютой в конце
#     Args:
#         price (float): положительное число для перевода в денежный эквивалент

#     Returns:
#         str: денежный эквивалент
#     """
#     try:
#         format_price = ""

#         if float(price) < 0:
#             raise ValueError("Ожидается положительное число!")
#         else:
#             corr_price = (f"{corr_price:_}").replace("_", " ")
#             float_path = corr_price.split()[-1]

#             if int(float_path):
#                 corr_float_path = f"{float_path}.00"

#             if len(float_path.split(".")[1]) < 2:
#                 corr_float_path = f"{float_path}0"
#             else:
#                 corr_float_path = f"{float(float_path):.2f}"

#             float_path = corr_float_path

#             format_price = " ".join(corr_price)

#         return format_price
#     except Exception as e:
#         print(f"Ошибка {type(e).__name__}: {str(e)}")


# print(format_in_monetary_rub(265))


def format_in_monetary_rub(price: float) -> str:
    """
    Возвращает число в виде денежной величины
    с разделителями групп разрядов в качестве пробела и валютой 'руб.' в конце.

    Args:
        price (float): положительное число для перевода в денежный эквивалент

    Returns:
        str: денежный эквивалент в формате "X XXY.ZZ руб."
    """
    try:
        if float(price) < 0:
            raise ValueError("Ожидается положительное число!")

        rounded_price = round(float(price), 2)
        str_price = str(rounded_price)

        # работа с дробной частью
        if "." in str_price:
            integer_part, decimal_part = str_price.split(".")
            decimal_part = decimal_part.ljust(2, "0")[:2]
        else:
            integer_part = str_price
            decimal_part = "00"

        # работа с целой частью
        reversed_integer = integer_part[::-1]
        groups = [
            reversed_integer[i : i + 3]
            for i in range(
                0, len(reversed_integer), 3
            )  # переворачиваем строку для удобного деления по 3 знака
        ]
        formatted_integer = " ".join(groups)[::-1]  # возвращаем в исходное

        result = f"{formatted_integer}.{decimal_part} руб."
        return result

    except ValueError as e:
        if "Ожидается положительное число!" in str(e):
            raise
        else:
            raise TypeError("Ожидается число (int или float).")
    except Exception as e:
        print(f"Неизвестная ошибка {type(e).__name__}: {str(e)}")
        return None


print(format_in_monetary_rub(0))
print(format_in_monetary_rub(1234.556478))
print(format_in_monetary_rub(1000000.99))
print(format_in_monetary_rub(123))
print(format_in_monetary_rub(-123))
