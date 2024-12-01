from random import randrange, choice
from turtle import Turtle, Screen

def get_random_color():
    return (randrange(255),randrange(255),randrange(255))

def get_random_direction_in_deg():
    return choice([0, 90, 180, 270])

# setup screen
screen = Screen()
screen.colormode(255)
t = Turtle()
t.pensize(10)
t.speed(10)

step_size = 20
number_of_steps = 1000

for i in range(0,number_of_steps):
    t.color(get_random_color())
    t.setheading(get_random_direction_in_deg())
    t.forward(step_size)

screen.exitonclick()
