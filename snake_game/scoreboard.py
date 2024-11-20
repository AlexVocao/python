from turtle import Turtle

CENTER = "center"
LEFT = "left"
RIGHT = "right"
COURIER_FONT = ("courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=CENTER, font=COURIER_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=CENTER, font=("courier", 24, "bold"))

    def increases_score(self):
        self.score += 1
        self.clear()
        self.update_score()

