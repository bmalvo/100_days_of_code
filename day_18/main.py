import random
from turtle import Turtle, Screen
from random_color import random_color
from draw_rectangle import draw_rectangle
from draw_dash_line import draw_dash_line
from draw_decagon import draw_decagon
from draw_nonagon import draw_nonagon
from draw_octagon import draw_octagon
from draw_heptagon import draw_heptagon
from draw_hexagon import draw_hexagon
from draw_pentagon import draw_pentagon
from draw_square import draw_square
from draw_triangle import draw_triangle


tim = Turtle()
tim.shape('turtle')
tim.color('chartreuse')

def tim_new_color():
    return tim.color(random_color())

# draw a rectangle
# draw_rectangle(tim)

# draw a dash-line
# draw_dash_line(tim)

# # draw a triangle
# tim_new_color()
# draw_triangle(tim)

# # draw a square
# tim_new_color()
# draw_square(tim)

# # draw a pentagon
# tim_new_color()
# draw_pentagon(tim)

# # draw a hexagon
# tim_new_color()
# draw_hexagon(tim)

# # draw a heptagon
# tim_new_color()
# draw_heptagon(tim)

# # draw an octagon
# tim_new_color()
# draw_octagon(tim)

# # draw a nonagon
# tim_new_color()
# draw_nonagon(tim)

# # draw a decagon
# tim_new_color()
# draw_decagon(tim)

# Random walk

directions_list = [0, 90, 180, 270]
tim.pensize(10)
tim.speed(0)
for i in range(500):
    tim_new_color()
    tim.setheading(random.choice(directions_list))
    tim.forward(50)

screen = Screen()
screen.exitonclick()
