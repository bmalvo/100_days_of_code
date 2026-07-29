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

def tim_new_color():
    return tim.color(random_color())

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
tim_new_color()
for i in range(3):
    tim.forward(100)
    tim.right(120)
# draw a square
tim_new_color()
for i in range(4):
    tim.forward(100)
    tim.right(90)
# draw a pentagon
tim_new_color()
for i in range(5):
    tim.forward(100)
    tim.right(72)
# draw a hexagon
tim_new_color()
for i in range(6):
    tim.forward(100)
    tim.right(60)
# draw a heptagon
tim_new_color()
for i in range(7):
    tim.forward(100)
    tim.right(51.4)

screen = Screen()
screen.exitonclick()
