from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


the_game_is_on = True

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.setup(width=800, height=600)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while the_game_is_on:
    scoreboard.update_score()
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()
    if ball.xcor() > 390:
        scoreboard.l_scores()
        ball.reset_position()
    if ball.xcor() < -390:
        scoreboard.r_scores()
        ball.reset_position()

screen.exitonclick()