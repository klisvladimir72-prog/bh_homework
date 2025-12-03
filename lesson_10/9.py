"""
Написать функцию hello, которая принимает 2 аргумента name и surname и
выводит принтом "Привет, {name} {surname}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
Выполняеся функция <имя> с аргусентами <аргументы> 
После выполнения функции напечатать строку "<имя функции> - завершена"
"""

from functools import wraps


def log_decorator(func):
    """
    Декоратор для логирования аргументов фнкции.

    Вывод аргументов функции и отслеживание окончания функции.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__

        args_str = ', '.join(repr(arg) for arg in args)
        kwargs_str = ', '.join(f"{k}={repr(v)}" for k, v in kwargs.items())

        all_args=[]
        
        if args_str:
            all_args.append(args_str)
        if kwargs_str:
            all_args.append(kwargs_str)
            
        args_repr = ', '.join(all_args)
        
        print(f"Выполняется функция {func_name} с аргументами {args_repr}")
        
        result = func(*args, **kwargs)
        
        print(f"{func_name} - завершена")
        
        return result
    return wrapper


@log_decorator
def hello(name, surname):
    """
    Функция, выводящая приветствие.
    """
    print(f"Привет, {name} {surname}")



hello("Иван", "Петров")  
print()
hello(name="Мария", surname="Сидорова") 
