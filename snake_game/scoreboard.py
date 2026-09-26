from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.print_board()

    def print_board(self):
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f'Score: {self.score}', align= 'center', font=('Arial', 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.print_board()
