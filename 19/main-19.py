from turtle import Turtle, Screen

FORWARD_STEP_SIZE = 10
FORWARD_STEP_SIZE = 10
FORWARD_STEP_SIZE = 10
FORWARD_STEP_SIZE = 10
FORWARD_STEP_SIZE = 10
FORWARD_STEP_SIZE = 10
TURN_SIZE = 10





t = Turtle()
s = Screen()

s.listen()

def move_forward():
    t.forward(FORWARD_STEP_SIZE)

def turn_left():
    t.left(TURN_SIZE)

def turn_right():
    t.right(TURN_SIZE)

def clear_screen():
    t.reset()

def move_backward():
    t.backward(FORWARD_STEP_SIZE)

s.onkey(key="w",fun=move_forward)
s.onkey(key="a" , fun=turn_left )
s.onkey(key="s" , fun=move_backward )
s.onkey(key="d" , fun=turn_right )
s.onkey(key="c" , fun=clear_screen )
s.exitonclick()
