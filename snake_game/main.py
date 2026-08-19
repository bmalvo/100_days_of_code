from turtle import Screen, Turtle


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('snake game')

starting_positions = [(0,0), (-20,0), (-40,0)]

for sp in starting_positions:
    segment = Turtle(shape='square')
    segment.color('white')
    segment.goto(sp)



screen.exitonclick()