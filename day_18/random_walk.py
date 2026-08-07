import random
from new_color import new_color

def random_walk(turtle):
    directions_list = [0, 90, 180, 270]
    turtle.pensize(10)
    turtle.speed(0)
    for i in range(500):
        new_color(turtle)
        turtle.setheading(random.choice(directions_list))
        turtle.forward(50)
