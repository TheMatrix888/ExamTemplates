from turtle import *
tracer(1000)
left(90)
down()
m = 10

for i in range(2):
    forward(21*m)
    right(90)
    forward(27*m)
    right(90)
up()
forward(9*m)
right(90)
forward(10*m)
left(90)
down()
for i in range(2):
    forward(86*m)
    right(90)
    forward(47*m)
    right(90)

up()
for x in range(-10, 50):
    for y in range(-10, 50):
        goto(x*m, y*m)
        dot(4, "red")

input()