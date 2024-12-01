from random import randrange
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
t = Turtle()
current_shape_degrees = 360
shape_edge_length = 100
largest_number_of_edges = 10
for i in range(3, largest_number_of_edges):
    current_shape_degrees = 360 / i
    t.color(randrange(255),randrange(255),randrange(255))
    for edges in range(0,i):
        t.forward(shape_edge_length)
        t.right(current_shape_degrees)

screen.exitonclick()
