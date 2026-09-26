from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('snake game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.print_board()

#     detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.clear()

screen.exitonclick()
