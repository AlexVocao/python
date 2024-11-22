from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("orange")

        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-300, 260)
        self.write(f"Level: {self.score}", align="left", font=("courier", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("courier", 60, "bold"))
