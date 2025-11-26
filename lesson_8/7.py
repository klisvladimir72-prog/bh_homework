"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку
и возвращает словарь, который содержит информацию о количестве
символов, слов, строк и предложений в тексте.
Затем создайте вторую функцию, которая принимает этот словарь,
и выводит его содержимое в удобном и красивом формате.

"""


def analyze_text(text: str) -> dict:
    """
    Принимает текстовую строку и возвращает словарь с количеством:
    - символов (включая пробелы и знаки препинания),
    - слов,
    - строк,
    - предложений.

    Args:
        text (str): входной текст

    Returns:
        dict: {'characters': int, 'words': int, 'lines': int, 'sentences': int}
    """
    characters = len(text)

    lines = text.count("\n") + 1

    words = len(text.split())

    sentences = 0
    for char in text:
        if char in ".!?":
            sentences += 1

    return {
        "characters": characters,
        "words": words,
        "lines": lines,
        "sentences": sentences,
    }


def print_analysis(stats: dict) -> None:
    """
    Выводит содержимое словаря с анализом текста в удобном формате.

    Args:
        stats (dict): словарь с результатами анализа
    """
    print("Анализ текста:")
    print(f"  Количество символов: {stats['characters']}")
    print(f"  Количество слов: {stats['words']}")
    print(f"  Количество строк: {stats['lines']}")
    print(f"  Количество предложений: {stats['sentences']}")


text = """Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quasi quam quibusdam laborum ea ad\n
odio minus, eaque nulla id tenetur incidunt. Nobis nihil consequatur qui aliquam explicabo\n
natus recusandae ex."""

stats = analyze_text(text)
print_analysis(stats)
