"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0.
Выдать средний бал ученика.
"""

import statistics
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

mark_list = []

console.print(
    Panel(
        "[bold blue]💡 Для расчета среднего балла введите '0'[/]",
        title="Оценки ученика",
        width=80,
    )
)

while True:
    mark_schoolboy = console.input("Введите оценку ученика: ").strip()

    if mark_schoolboy == "0":
        break

    if not mark_schoolboy:
        console.print("⚠️  Вы забыли ввести оценку.", style="bold yellow")
        continue

    try:
        mark = int(mark_schoolboy)
        if 0 < mark < 11:
            mark_list.append(mark)
        else:
            raise ValueError(f"❌ Оценка должна быть от 1 до 10!")

    except ValueError as e:
        if "Оценка должна быть от 1 до 10" in str(e):
            console.print(str(e), style="bold red")
        else:
            console.print("❌ Необходимо ввести число!", style="bold red")
        continue

if mark_list:
    average = statistics.mean(mark_list)

    table = Table(
        title=f"\nОценки ученика", show_header=True, header_style="bold magenta"
    )
    table.add_column("Номер", style="dim", width=6)
    table.add_column("Оценка", justify="center")

    for i, mark in enumerate(mark_list, 1):
        table.add_row(str(i), str(mark))

    console.print(table)

    console.print(
        Panel(
            f"[bold green]Средний балл: {average:.1f}[/]",
            title="[bold cyan]📊 Результат",
            expand=False,
        )
    )
else:
    console.print(
        Panel(
            "[bold red]❌ Нет оценок для расчёта среднего балла.[/]",
            title="Ошибка",
            width=80,
        )
    )
