from random import choice
from turtle import Turtle, Screen

import colorgram

s = Screen()
t = Turtle()
DOTS_WIDTH  = 10
DOTS_HEIGHT = 10

s.colormode(255)
t.speed(0)
t.pensize(5)
t.penup()
t.setposition(-200,200)
t.hideturtle()

#colors = colorgram.extract(".\\18\\hirsh-painting\\image.jpg", 32)
#rgb_colors = []
#for item in colors:
#    (r, g, b) = item.rgb
#    rgb_colors.append((r,g,b))
#print(rgb_colors)

rgb_colors = [
        (203, 163, 126), (235, 242, 247), (162, 167, 34), (235, 68, 127), (149, 51, 98), (236, 78, 53), 
        (12, 144, 67), (238, 218, 78), (226, 115, 161), (9, 140, 181), (128, 31, 82), (62, 196, 223), 
        (24, 174, 136), (167, 58, 50), (250, 231, 0), (25, 192, 214), (115, 187, 151), (241, 162, 186), 
        (148, 221, 194), (238, 175, 158), (1, 116, 22), (126, 219, 232), (79, 16, 72), (128, 40, 38)
        ]

for j in range(0,DOTS_HEIGHT):
    for i in range(0,DOTS_WIDTH):
        t.dot(20,choice(rgb_colors))
        t.penup()
        t.forward(40)
        t.pendown()
    t.penup()
    t.setheading(270)
    t.forward(40)
    t.setheading(0 if j % 2 == 1 else 180)
    t.forward(40)

s.exitonclick()
