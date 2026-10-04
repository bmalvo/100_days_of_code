from turtle import Screen, Turtle

# 1. Create a screen

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('pink')
screen.title('PONG')
screen.tracer(0)

# 2. Create and move a paddle

right_paddle = Turtle()
right_paddle.penup()
right_paddle.shape('square')
right_paddle.color('white')
right_paddle.shapesize(5, 1)
right_paddle.setpos(350, 0)

def right_paddle_up():
    new_y = right_paddle.ycor() + 20
    return right_paddle.goto(right_paddle.xcor(), new_y)

def right_paddle_down():
    new_y = right_paddle.ycor() - 20
    return right_paddle.goto(right_paddle.xcor(), new_y)

screen.listen()
screen.onkey(right_paddle_up, 'Up')
screen.onkey(right_paddle_down, 'Down')



# 3. Create another paddle
# 4. Create a ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score

game_is_on = True


while game_is_on:
    screen.update()

screen.exitonclick()
