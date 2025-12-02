'''

**для самых любопытных

Лучше всего запускать в консоли виндовс
она имеет 30 строк - как раз один кадр

Данный пример генерирует каждый кадр случайный набор снежинок.
т.е. снежинки не падают а просто случайно появляются в разных местах

Переделать программу так чтобы каждый кадр каждая существующая 
снежинка опускалась вниз, а сверху генерировались новые.

Дополнительные варианты:
    - снежинки могут быть разные (* . + Ж)
    - крупные снежинки падают быстрей
    - иногда меняется ветер и снежинки летят или прямо или в любую сторону
    - снежинки при генерации не должны быть рядом (слипаться) 

'''


import os
import random
import time


# Возможные символы снежинок
SNOWFLAKE_TYPES = ['*', '.', '+', 'Ж']

# Скорость падения: крупные (Ж) падают быстрее
SNOWFLAKE_SPEED = {
    '*': 1,
    '.': 1,
    '+': 1,
    'Ж': 2,
}


def c_tree(rows, snowflakes):
    # Создаём пустой экран
    screen = [[" "] * (2 * rows) for _ in range(rows)]

    # Рисуем елочку
    for i in range(rows):
        start = rows - i - 1
        end = rows + i
        for j in range(start, end + 1):
            if j < len(screen[i]):
                screen[i][j] = "*" if j != start and j != end else " "

    # Рисуем снежинки
    for x, y, char in snowflakes:
        if 0 <= y < rows and 0 <= x < len(screen[0]):
            screen[y][x] = char

    tree_txt = "\n".join("".join(line) for line in screen)
    return tree_txt


def update_snowflakes(snowflakes, rows, cols, wind=0):
    updated = []
    for x, y, char in snowflakes:
        new_y = y + SNOWFLAKE_SPEED[char]
        new_x = x + wind
        # Если снежинка упала за экран — убираем
        if new_y < rows:
            updated.append((new_x, new_y, char))
    return updated


def generate_new_snowflakes(snowflakes, rows, cols, count=5):
    existing_positions = {(x, y) for x, y, _ in snowflakes}
    new_snowflakes = []
    for _ in range(count):
        x = random.randint(0, cols - 1)
        y = 0
        tries = 0
        # Проверяем, чтобы не слипались
        while (x, y) in existing_positions and tries < 100:
            x = random.randint(0, cols - 1)
            tries += 1
        if tries < 100:
            char = random.choice(SNOWFLAKE_TYPES)
            new_snowflakes.append((x, y, char))
    return new_snowflakes


def main():
    rows = 30
    cols = 2 * rows
    snowflakes = []

    while True:
        os.system('cls')

        # Обновляем ветер раз в 5-10 кадров
        if random.randint(1, 10) == 1:
            wind = random.choice([-1, 0, 1])
        else:
            wind = 0

        # Обновляем позиции снежинок
        snowflakes = update_snowflakes(snowflakes, rows, cols, wind)

        # Добавляем новые снежинки сверху
        new_flakes = generate_new_snowflakes(
            snowflakes, rows, cols, count=random.randint(1, 5))
        snowflakes.extend(new_flakes)

        # Рисуем кадр
        frame = c_tree(rows, snowflakes)
        print(frame)

        time.sleep(0.1)


if __name__ == "__main__":
    main()
   