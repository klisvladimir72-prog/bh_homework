"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"

Написать функцию beef, которая:
 - печатает "### говядина ###"

Написать функцию chicken, которая:
 - печатает "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""


# Результат

# == Гамбургер ==
# </------------\>
# ----- лук ------
# *** помидоры ****
# ### говядина ###
# <\____________/>


# == Чикенбургер ==
# </------------\>
# ^^^^^ сыр ^^^^^^
# ~~~~ салат ~~~~~
# |||| курица ||||
# <\____________/>


from functools import wraps


def bread(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("</------------\>")
        result = func(*args, **kwargs)
        print("<\____________/>")
        return result
    return wrapper

def tomato(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("*** помидоры ****")
        return func(*args, **kwargs)
    return wrapper

def salad(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("~~~~ салат ~~~~~")
        return func(*args, **kwargs)
    return wrapper

def cheese(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("^^^^^ сыр ^^^^^^")
        return func(*args, **kwargs)
    return wrapper

def onion(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("----- лук ------")
        return func(*args, **kwargs)
    return wrapper


def beef():
    print("### говядина ###")

def chicken():
    print("|||| курица ||||")



@bread
@onion
@tomato
def burger():
    beef()
    
    
    
@bread
@cheese
@salad    
def chicken_burger():
    chicken()
    
print("==Гамбургер==")
burger()
print("\n==Чикенбургер==")
chicken_burger()