from turtle import *
bgcolor("black")
pencolor("white")
tracer(100)
m = 0.5

left(90)
up()

right(270)
forward(350*m)
right(270)
forward(50*m)
right(180)
down()

for i in range(20):
    forward(530*m)
    right(90)
    forward(380*m)
    right(90)

up()
right(90)
forward(10*m)
right(90)
forward(20*m)
right(270)
down()

for i in range(32):
    forward(830*m)
    right(270)
    forward(530*m)
    right(270)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(2, "red")

input()

# UNSOLVED
# https://education.yandex.ru/ege/variants/7abf7990-4043-4fe4-b5ce-bcc69d714df9/task/6