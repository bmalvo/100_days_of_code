from turtle import Turtle, Screen


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
for i in range(3):
    tim.forward(100)
    tim.right(120)


screen = Screen()
screen.exitonclick()
