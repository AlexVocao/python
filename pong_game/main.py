import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

dash_line = Turtle()
dash_line.hideturtle()
dash_line.setheading(90)
dash_line.color("white")
dash_line.penup()
dash_line.goto(0, -250)
dash_line.pendown()

for i in range(25):
    dash_line.forward(10)
    dash_line.penup()
    dash_line.forward(10)
    dash_line.pendown()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")


is_new_round = False
while scoreboard.rounds > 0:
    screen.update()
    time.sleep(ball.speed)
    ball.move()

    # Detect collision of ball & paddle
    if l_paddle.distance(ball) < 50 and (ball.xcor() - l_paddle.xcor()) < 20:
        ball.bounce_x()
    elif r_paddle.distance(ball) < 50 and (r_paddle.xcor() - ball.xcor()) < 20:
        ball.bounce_x()
    elif ball.xcor() >= 380:
        scoreboard.increase_score_l()
        is_new_round = True
    elif ball.xcor() <= -380:
        scoreboard.increase_score_r()
        is_new_round = True
    elif ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if is_new_round:
        ball.reset_position()
        is_new_round = False

scoreboard.show_winner()
screen.exitonclick()
