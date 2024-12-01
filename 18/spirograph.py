from random import randrange 
from turtle import Turtle, Screen

def get_random_color():
    return (randrange(255),randrange(255),randrange(255))


# setup screen
screen = Screen()
screen.colormode(255)
t = Turtle()
#t.pensize(10)
t.speed(0)

number_of_circles = 100
circle_radius = 100
turn_degrees = 360 / number_of_circles

for i in range(0, number_of_circles):
    t.color(get_random_color())
    t.circle(circle_radius)
    t.left(turn_degrees)
    

screen.exitonclick()
