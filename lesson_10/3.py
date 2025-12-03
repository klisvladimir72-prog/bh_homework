"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""

def check_brackets(str:str)->bool:
    """
    Проверка правильности открытия и закрытия скобок в строке.

    Args:
        str (str): произвольная строка

    Returns:
        bool: True -> скобки расставлены правильно
              False -> не хватает какой-то скобки
    """
    
    count_correct = 0
    for char in str:
        if char == "(":
            count_correct +=1
        if char == ")":
            count_correct -=1
            if count_correct < 0:
                return False
        
    return count_correct == 0


print(check_brackets("(()())"))
print(check_brackets("(()()()"))
print(check_brackets("(hello(2)ver()(33)python)"))
print(check_brackets("(hello(2()ver(33)python))"))
print(check_brackets("(hello(2()ver(33)python)"))
