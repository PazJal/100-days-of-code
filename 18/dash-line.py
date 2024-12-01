from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
pen_is_down = True
for i in range (0, 20):
    pen_is_down = not pen_is_down
    if pen_is_down:
        timmy_the_turtle.penup()
    else: 
        timmy_the_turtle.pendown()

    timmy_the_turtle.forward(20)

screen = Screen()
screen.exitonclick()
