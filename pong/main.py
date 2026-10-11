from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

# 1. Create a screen

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('pink')
screen.title('PONG')
screen.tracer(0)

# 2. Create and move a paddle
# 2.1 create a paddles from a paddle class
# 3. Create another paddle

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.paddle_up, 'Up')
screen.onkey(r_paddle.paddle_down, 'Down')
screen.onkey(l_paddle.paddle_up, 'w')
screen.onkey(l_paddle.paddle_down, 's')




# 4. Create a ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score

game_is_on = True


while game_is_on:
    time.sleep(1/10)
    screen.update()
    ball.move()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()

screen.exitonclick()
