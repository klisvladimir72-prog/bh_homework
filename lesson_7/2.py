"""
Запросить фразу состоящую минимум из трех слов.
Сформировать фразу из этих слов в которой каждая буква слова,
продублирована то количество раз, которое соответствует номеру позиции
данной буквы в слове этой буквы.
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

"""

from pprint import pprint


def duplicate_letters(word: str) -> str:
    return "".join(char * (key + 1) for key, char in list(enumerate(word)))


while True:
    user_input = input(f"Введите фразу минимум из трех слов: \n").strip()

    words_list = list(user_input.split())

    if len(words_list) >= 3:
        new_phrase = " ".join(duplicate_letters(word) for word in words_list)
        print(new_phrase)
        break

    print(f"❌ Фраза должна состоять минимум из трех слов!")
    continue
