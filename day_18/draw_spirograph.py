from new_color import new_color

def draw_spirograph(turtle):
    tilt = 0
    turtle.speed(0)
    for i in range(int(360 / 5)):
        new_color(turtle)
        turtle.left(tilt + 5)
        turtle.circle(100)
