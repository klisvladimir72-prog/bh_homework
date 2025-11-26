"""
*
Написать программу калькулятор которая предлагает
ввести пример для решения пока пользователь не введет команду "стоп"
Программа должна решить пример и запросить следующий.
При вводе команды "стоп" программа завершается.
Поддерживаемые операции: + - * ** /
Пример:
    Введите пример или 'стоп' для завершения: 2 + 2
    Ответ: 4
    Введите пример или 'стоп' для завершения: 16 / 8
    Ответ: 2
    Введите пример или 'стоп' для завершения: 1651+
    Неправильный формат. Пример: '2 + 4'


eval() exec() нельзя
"""

from rich.console import Console
from rich.panel import Panel
from colorama import Fore, Style

OPERATORS_PRIORITY = [["**"], ["*", "/"], ["-", "+"]]
console = Console()

test_input = "3 * 4 ** 2 - -3 / 0.25 + -2 ** 0.5"


# проверка
def validation_expression():
    while True:
        calc = list(
            input(
                f"{Fore.BLUE}Введите выражение формата (2 + 3 * 4 ** 5 / 6): {Style.RESET_ALL}"
            ).split()
        )

        flag_valid = True
        calc_2 = ""

        if calc[0] in ["stop", "ыещз"]:
            print(f"{Fore.LIGHTRED_EX}Вы вышли из программы!{Style.RESET_ALL}")
            exit()

        if len(calc) < 3 or not len(calc) % 2:
            flag_valid = False
            print(
                f"⚠️  {Fore.YELLOW}Вы ввели выражение не полностью или с ошибкой!{Style.RESET_ALL}\n"
            )
            continue

        for i, val in enumerate(calc, 1):
            if i % 2:
                try:
                    float(val)
                except ValueError:
                    print(
                        f"{Fore.RED}❌ {calc_2}: {Fore.RED}{val}{Style.RESET_ALL} - здесь ожидается число!"
                    )
                    print(
                        f"{Fore.YELLOW}⚠️ Введите выражение согласно заданного формата через пробел!\n{Style.RESET_ALL}"
                    )
                    flag_valid = False
                    break
            else:
                if val not in ["**", "*", "/", "-", "+"]:
                    print(
                        f"❌ Недопустимый оператор в выражении - {Fore.RED}{val}{Style.RESET_ALL}"
                    )
                    print(
                        f"{Fore.YELLOW}⚠️ Введите выражение согласно заданного формата через пробел!\n{Style.RESET_ALL}"
                    )
                    flag_valid = False
                    break
        calc_2 += val

        if flag_valid:
            break

    return calc


def calculate_expression(expr):
    expr_copy = expr[:]
    # определяем приоритет действий
    for op_group in OPERATORS_PRIORITY:
        while any(op in expr_copy for op in op_group):
            op_flag = False
            for i, val in enumerate(expr_copy):
                # ищем действие для выполнения
                if val in op_group:
                    left = float(expr_copy[i - 1])
                    right = float(expr_copy[i + 1])

                    # проверка деления на 0
                    if val == "/" and right == 0:
                        print(
                            f"{' '.join(expr_copy[:i-1])} {Fore.RED}{" ".join(expr_copy[i-1:i+2])}{Style.RESET_ALL} {" ".join(expr_copy[i+2:])} "
                        )
                        print(f"{Fore.RED}⚠️  Делить на 0 нельзя!!! {Style.RESET_ALL}")
                        return None

                    match val:
                        case "**":
                            try:
                                result_val = left**right
                                if isinstance(result_val, complex):
                                    print(
                                        f"{Fore.RED}⚠️  Результат {Fore.CYAN}{left} ** {right} {Fore.RED}не является действительным числом! {Style.RESET_ALL}"
                                    )
                                    return None
                                if (
                                    abs(result_val) == float("inf")
                                    or result_val != result_val
                                ):
                                    print(
                                        f"{Fore.RED}⚠️  Результат слишком большой или недопустимый! {Style.RESET_ALL}"
                                    )
                                    return None
                                result = str(round(result_val, 4))
                            except OverflowError:
                                print(
                                    f"{Fore.RED}⚠️  Результат слишком большой! {Style.RESET_ALL}"
                                )
                                return None
                        case "*":
                            result = str(left * right)
                        case "/":
                            result = str(left / right)
                        case "+":
                            result = str(left + right)
                        case "-":
                            result = str(left - right)

                    expr_copy[i - 1 : i + 2] = [result]
                    op_flag = True
                    break
            if not op_flag:
                break
    return float(expr_copy[0])


console.print(
    Panel(
        "[bold blue]💡 Для выхода из программы введите 'stop'.",
        title="Вычисление выражения",
        width=80,
    )
)
while True:
    expression = validation_expression()
    result = calculate_expression(expression)

    if result is not None:
        console.print(f"Ответ: {result}")
