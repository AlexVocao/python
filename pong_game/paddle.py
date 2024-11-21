from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.step = 40
        self.speed("fastest")

    def move_up(self):
        new_y = self.ycor() + self.step
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - self.step
        self.goto(self.xcor(), new_y)
