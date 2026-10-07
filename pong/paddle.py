from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.setpos(x_cor, y_cor)

    def paddle_up(self):
        self.y_cor = self.y_cor + 20
        return self.goto(self.x_cor, self.y_cor)

    def paddle_down(self):
        self.y_cor = self.y_cor -20
        return self.goto(self.x_cor, self.y_cor)
