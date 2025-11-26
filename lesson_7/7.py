"""
Запросить любое число не менее 10. 
Вывести на экран сумму квадратов каждой цифры составляющей это число. 
Например: дано 236 => 2*2 + 3*3 + 6*6 = 49 

"""


from rich.console import Console

console = Console()

while True:
    user_input = input("Введите число не менее 10: ").strip()

    try:
        number = int(user_input)

        if number < 10:
            console.print("⚠ Число должно быть не менее 10.",
                          style="bold yellow")
            continue

        digits = [int(d) for d in str(number)]
        squares = [d ** 2 for d in digits]
        total = sum(squares)
        
        sum_squares = ''
        for dig in digits:
            sum_squares += f" {dig}**2 +"
        
        console.print(f"{sum_squares[:-1].strip()} = {total}")
        break

    except ValueError:
        console.print("❌ Введите корректное целое число!", style="bold red")
        continue
