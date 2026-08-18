from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width= 500, height= 400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
is_race_on = False

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

red = Turtle()
red.shape('turtle')
red.color('red')
red.penup()
red.goto(x= -230, y= -100)
turtles.append(red)

orange = Turtle()
orange.shape('turtle')
orange.color('orange')
orange.up()
orange.goto(x= -230, y= -60)
turtles.append(orange)

yellow = Turtle()
yellow.shape('turtle')
yellow.color('yellow')
yellow.penup()
yellow.goto(x= -230, y= -20)
turtles.append(yellow)

green = Turtle()
green.shape('turtle')
green.color('green')
green.penup()
green.goto(x= -230, y= 20)
turtles.append(green)

blue = Turtle()
blue.shape('turtle')
blue.color('blue')
blue.penup()
blue.goto(x= -230, y= 60)
turtles.append(blue)

purple = Turtle()
purple.shape('turtle')
purple.color('purple')
purple.penup()
purple.goto(x= -230, y= 100)
turtles.append(purple)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f'You win! The {winning_turtle} turtle is the winner!')
            else:
                print(f'You lose! The {winning_turtle} turtle is the winner!')

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
