from turtle import *
tracer(10)
m = 20
left(90)
down()

for i in range(2):
    forward(10*m)
    right(90)
    forward(18*m)
    right(90)
up()
forward(5*m)
right(90)
forward(14*m)
left(90)
down()
for i in range(2):
    forward(17*m)
    right(90)
    forward(7*m)
    right(90)

up()
for x in range(-10, 100):
    for y in range(-10, 100):
        goto(x*m, y*m)
        dot(5)

input()