"""
Запросить фразу
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""

from collections import Counter
import re


phrase = input("Введите фразу: ").strip()

if not phrase:
    print("❌ Вы ввели пустую строку.")
else:
    unique_chars = set(phrase)
    print(f"\nКоличество уникальных символов: {len(unique_chars)}")

    words = re.findall(r"[a-zA-Zа-яА-ЯёЁ]+", phrase.lower())
    unique_words = set(words)
    print(f"Количество уникальных слов: {len(unique_words)}")

    if phrase.strip():
        char_count = Counter(phrase)
        most_common_char, max_count = char_count.most_common(1)[0]
        print(
            f"Символ, встречающийся чаще всего: '{most_common_char}' (встретился {max_count} раз)"
        )
    else:
        print("Нечего анализировать.")
