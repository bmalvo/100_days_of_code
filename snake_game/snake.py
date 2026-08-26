from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []

        starting_positions = [(0,0), (-20,0), (-40,0)]


        for sp in starting_positions:
            segment = Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto(sp)
            self.segments.append(segment)

    def move(self):

        for seg in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg -1].xcor()
            new_y = self.segments[seg -1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)