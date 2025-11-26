"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


store_reviews = {}

console.print(Panel(
    "[bold blue]💡 Для выхода из программы введите 'stop'.", title="Отзывы о магазине", width = 80))

while True:
    name = input("Введите Ваше имя: ").strip().title()
    if name.lower() in [ 'stop', 'ыещз']:
        break
    
    review = input(f"Напишите отзыв о магазине: \n").strip().capitalize()   
    if review.lower() in [ 'stop', 'ыещз']:
        break

    store_reviews[name] = review
    continue

console.print(f"\nКоличество отзывов: [bold] {len(store_reviews)}[/]\n")

names = list(store_reviews.keys())
table_names = Table(title='Имена пользователей',
                    show_header=True, header_style="bold magenta")
table_names.add_column("№", style='dim', width=4)
table_names.add_column("Имя",  justify='left')

for i, name in enumerate(names, 1):
    table_names.add_row(str(i), name)

console.print(table_names)


reviews = list(store_reviews.values())
table_reviews = Table(title='Отзывы', show_header=True,
                      header_style="bold cyan")
table_reviews.add_column("№", style="dim", width=4)
table_reviews.add_column("Отзыв", justify='left')

for i, review in enumerate(reviews, 1):
    table_reviews.add_row(str(i), review)

console.print(table_reviews)
