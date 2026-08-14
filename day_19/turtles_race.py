from turtle import Turtle, Screen

screen = Screen()
screen.setup(width= 500, height= 400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

red = Turtle()
red.shape('turtle')
red.color('red')
red.penup()
red.goto(x= -230, y= -100)

orange = Turtle()
orange.shape('turtle')
orange.color('orange')
orange.up()
orange.goto(x= -230, y= -60)

yellow = Turtle()
yellow.shape('turtle')
yellow.color('yellow')
yellow.penup()
yellow.goto(x= -230, y= -20)

green = Turtle()
green.shape('turtle')
green.color('green')
green.penup()
green.goto(x= -230, y= 20)

blue = Turtle()
blue.shape('turtle')
blue.color('blue')
blue.penup()
blue.goto(x= -230, y= 60)

purple = Turtle()
purple.shape('turtle')
purple.color('purple')
purple.penup()
purple.goto(x= -230, y= 100)

screen.exitonclick()
