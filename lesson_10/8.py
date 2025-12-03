"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название файла
"""

from functools import wraps


def handle_errors(file_name=None):
    """
    Декоратор, перехватывающий исключения в декорируемой функции.
    Вывод ошибок - Defaults to 'console' or to 'file'
    Args:
        file_name (_type_, optional): Defaults to None.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_msg = f"Ошибка в функции '{func.__name__}': {str(e)}"

                if file_name:
                    with open(file_name, 'a', encoding='utf-8') as f:
                        f.write(error_msg + '\n')
                else:
                    print(error_msg)
                
                return None
        
        return wrapper
    return decorator



@handle_errors()
def divide(a, b):
    return a / b


# 2. Вывод в файл
@handle_errors('errors.log')
def risky_function(x):
    return 10 / (x - 5)


# 3. Функция без ошибки
@handle_errors()
def safe_function():
    return "Всё ок"


# Примеры вызовов:

print("1. Вызов функции с делением на 0:")
divide(10, 0)  

print("\n2. Вызов risky_function с x=5:")
risky_function(5) 

print("\n3. Вызов безопасной функции:")
result = safe_function()
print(result)
