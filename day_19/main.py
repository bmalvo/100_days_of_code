from turtle import Turtle, Screen

leon = Turtle()
screen = Screen()


def move_forward():
    leon.forward(10)

def move_backward():
    leon.backward(10)

def move_counter_clockwise():
    leon.right(10)

def move_clockwise():
    leon.left(10)

def clear():
    leon.reset()

screen.listen()
screen.onkey(key = 'w', fun = move_forward)
screen.onkey(key = 's', fun = move_backward)
screen.onkey(key = 'd', fun = move_counter_clockwise)
screen.onkey(key = 'a', fun = move_clockwise)
screen.onkey(key = 'c', fun = clear)

screen.exitonclick()
