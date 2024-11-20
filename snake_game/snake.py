import time
from turtle import Turtle
import random

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
colors = ["red", "green", "blue"]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

directions = {RIGHT: LEFT, UP: DOWN, LEFT: RIGHT, DOWN: UP}

DISTANCE_STEP = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.speed = 0.5
        self.is_redirect = True

    def create_snake(self):
        for index in range(len(colors)):
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.goto(starting_positions[index])
            new_segment.color(colors[index])
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(DISTANCE_STEP)
        self.is_redirect = True

    def left(self):
        self.move_to(LEFT)

    def right(self):
        self.move_to(RIGHT)

    def up(self):
        self.move_to(UP)

    def down(self):
        self.move_to(DOWN)

    def move_to(self, direction):
        opp = directions.get(direction)
        if self.head.heading() != opp and self.is_redirect == True:
            self.head.setheading(direction)
            self.is_redirect = False

    def extend(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color(random.random(), random.random(), random.random())
        new_segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)

