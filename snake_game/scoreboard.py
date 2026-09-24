from mimetypes import init
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.score = score

    def print_board(self, score):
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f'Score: {score}', align= 'center', font=('Arial', 18, 'normal'))
        # self.write((200, 100))

