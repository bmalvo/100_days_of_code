from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('snake game')
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]

segments = []

for sp in starting_positions:
    segment = Turtle(shape='square')
    segment.color('white')
    segment.penup()
    segment.goto(sp)
    segments.append(segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1 / 4)
    for seg in range(len(segments) -1, 0, -1):
        new_x = segments[seg -1].xcor()
        new_y = segments[seg -1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].forward(20)




screen.exitonclick()