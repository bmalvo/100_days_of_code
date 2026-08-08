import colorgram
from turtle import Turtle, Screen

colors = colorgram.extract('hirst_painting.jpg', 240)
colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

leon = Turtle()
leon.shape('turtle')
leon.color('chartreuse')







screen = Screen()
screen.exitonclick()
