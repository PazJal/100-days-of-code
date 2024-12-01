from random import choice
from turtle import Turtle, Screen

import colorgram

s = Screen()
t = Turtle()

s.colormode(255)
t.speed(0)
t.pensize(5)

colors = colorgram.extract(".\\18\\hirsh-painting\\image.jpg", 16)
for j in range(0,20):
    for i in range(0,10):
        t.dot(20,choice(colors).rgb)
        t.penup()
        t.forward(40)
        t.pendown()
    t.penup()
    t.setheading(270)
    t.forward(40)
    t.setheading(0 if j % 2 == 1 else 180)

print(colors[0])

s.exitonclick()
