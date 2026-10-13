from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

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

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


#  detect collision with paddle
    if ball.distance(r_paddle) <  50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print('contact')
        ball.bounce_x()

#  right paddle miss the ball
    if ball.xcor() > 340:
        ball.restart_position()
        scoreboard.l_point()

#  left paddle missed the ball
    if ball.xcor() < - 340:
        ball.restart_position()
        scoreboard.r_point()

screen.exitonclick()
