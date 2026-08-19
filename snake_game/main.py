from turtle import Screen, Turtle


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('snake game')

snake1 = Turtle(shape='square')
snake1.color('white')
snake1.setpos(0, 0)

snake2 = Turtle(shape='square')
snake2.color('white')
snake2.setpos(-20, 0)

snake3 = Turtle(shape='square')
snake3.color('white')
snake3.setpos(-40, 0)


screen.exitonclick()