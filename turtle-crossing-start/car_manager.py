from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.penup()
        self.starting_position()

    def starting_position(self):
        y_position = random.randint(-230, 230)
        self.goto(300, y_position)

    def move(self):
        new_x_cor = self.xcor() - 10
        self.goto(new_x_cor, self.ycor())
