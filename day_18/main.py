from turtle import Turtle, Screen
import random


def random_color():
    r = round(random.random(), 3)
    g = round(random.random(), 3)
    b = round(random.random(), 3)
    return r, g, b


tim = Turtle()
tim.shape('turtle')
tim.color('chartreuse')

# draw a rectangle
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# draw a dash-line
# for i in range(15):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

# draw a triangle
tim.color(random_color())
for i in range(3):
    tim.forward(100)
    tim.right(120)


screen = Screen()
screen.exitonclick()
