import colorgram
from turtle import Turtle, Screen, colormode
from random import choice


colormode(255)

colors = colorgram.extract('hirst_painting.jpg', 240)
colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

leon = Turtle()
leon.shape('turtle')
leon.color('chartreuse')
leon.pu()
leon.setx(-360)
leon.sety(-280)

x = -360
y = -280

for _ in range(10):
    for _ in range(10):
        leon.dot(20, choice(colors))
        leon.fd(50)
    y += 50
    leon.teleport(x, y)


screen = Screen()
screen.exitonclick()
