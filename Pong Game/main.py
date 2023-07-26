from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

left_paddle = Paddle(-450, 0)
right_paddle = Paddle(450, 0)
ball = Ball()
score_board = Scoreboard()

left_paddle.move_on_command(up_key="w", down_key="s")
right_paddle.move_on_command(up_key="8", down_key="5")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 420 or \
            ball.distance(left_paddle) < 50 and ball.xcor() < -420:
        ball.bounce_x()
    #if ball misses the paddle
    if ball.xcor() > 500:
        ball.reset_position()
        score_board.l_point()

    if ball.xcor() < -500:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()
