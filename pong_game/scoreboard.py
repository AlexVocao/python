from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.rounds = 5
        self.goto(0, -300)
        self.update()

    def update(self):
        self.clear()
        self.goto(0, 260)
        self.write("SCORE", align="center", font=("courier", 30, "normal"))
        self.goto(0, 180)
        self.write(f"{self.l_score}  {self.r_score}", align="center", font=("courier", 80, "bold"))

    def increase_score_l(self):
        self.rounds -= 1
        self.l_score += 1
        self.update()

    def increase_score_r(self):
        self.rounds -= 1
        self.r_score += 1
        self.update()

    def show_winner(self):
        winner = ""

        if self.l_score > self.r_score:
            winner = "Player 1"
        elif self.l_score < self.r_score:
            winner = "Player 2"
        else:
            winner = "Draw"

        self.goto(0, 0)
        self.write(f"Winner", align="Center", font=("courier", 50, "normal"))
        self.goto(0, -150)
        self.write(winner, align="Center", font=("courier", 90, "bold"))
