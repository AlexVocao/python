import turtle
from random import random, randint
from turtle import Turtle

turtle.colormode(1)


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = 0.5

    def create_car(self):
        x = 300
        y = randint(-250, 250)
        if not self.is_cars_collision(x, y):
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color((random(), random(), random()))
            if car.pencolor() == "white":
                car.color((random(), random(), random()))
            car.setheading(180)
            car.goto(x, y)

            self.cars.append(car)

    def is_cars_collision(self, x, y):
        for car in self.cars:
            if (x - car.xcor()) < 60 and (y - car.ycor()) < 25:
                return True
        return False

    def move_cars(self):
        for car in self.cars:
            if car.xcor() < -420:
                y = randint(-250, 250)
                self.reset_position(car, y)
            else:
                car.forward(20)


    def reset_position(self, car, y):
        if not self.is_cars_collision(300, y):
            car.goto(300, y)

    def increase_speed(self):
        self.speed += 1