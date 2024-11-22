import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.title("Crossing Capstone Game")
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(car_manager.speed)

    if len(car_manager.cars) < 20:
        car_manager.create_car()

    car_manager.move_cars()

    # detect collision between player and cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            is_game_on = False

    if player.ycor() > 280:
        scoreboard.increase_score()
        car_manager.increase_speed()
        player.goto(0, -260)

screen.exitonclick()
