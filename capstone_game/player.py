from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.setheading(90)
        self.goto(0, -260)

    def move(self):
        self.forward(10)
