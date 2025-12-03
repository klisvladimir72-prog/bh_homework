"""
Добавить несколько черепах
    - или сразу
    * или в течении игры по одной через определенное количество кликов
    - на каждой забиндить клик через одну и туже функцию cath

"""

from turtle import *
from random import randint

ts = []
click_count = 0

width_screen = 800
height_screen = 600


def catch(x, y):
    global click_count
    click_count += 1

    clicked_turtle = None
    for t in ts:
        if abs(t.xcor() - x) < 10 and abs(t.ycor() - y) < 10:
            clicked_turtle = t
            break

    if clicked_turtle:
        clicked_turtle.goto(
            randint(-(width_screen // 2), width_screen // 2),
            randint(-(height_screen // 2), height_screen // 2),
        )
        clicked_turtle.left(randint(0, 360))

        if click_count % 5 == 0:
            add_new_turtle()


def add_new_turtle():
    """
    Создание новой черепахи со случайными параметрами цвета и поворота.
    """
    global ts
    new_turtle = Turtle("turtle")
    new_turtle.speed(10)
    new_turtle.color((randint(0, 255), randint(0, 255), randint(0, 255)))
    new_turtle.left(randint(0, 360))
    new_turtle.onclick(catch)
    ts.append(new_turtle)
    print(f"Добавлена новая черепаха. Всего: {len(ts)}")


# Настройка экрана
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Черепахи в атаке")
colormode(255)


for i in range(3):
    t = Turtle("turtle")
    t.speed(6)
    t.color((randint(0, 255), randint(0, 255), randint(0, 255)))
    t.left(randint(0, 360))
    t.onclick(catch)
    ts.append(t)


while True:
    for t in ts:
        t.forward(3)

        if abs(t.xcor()) > width_screen / 2:
            t.left(100)
        if abs(t.ycor()) > height_screen / 2:
            t.left(100)


mainloop()
