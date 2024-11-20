import time
from os import supports_bytes_environ
from turtle import Screen, Turtle

from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

is_game_over = False
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")


# define function =======================================
def is_snake_hit_food():
    return snake.head.distance(food) < 15


def is_snake_hit_wall():
    return snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280


def is_snake_hit_its_tail():
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 15:
            return True


def start_game():
    global is_game_over
    while not is_game_over:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # check snake hit food
        if is_snake_hit_food():
            scoreboard.increases_score()
            snake.extend()
            food.clear()
            food.refresh()

        # check snake hit wall or tail
        if is_snake_hit_wall() or is_snake_hit_its_tail():
            is_game_over = True
            scoreboard.game_over()


# define function =======================================

# call function
start_game()

screen.exitonclick()
