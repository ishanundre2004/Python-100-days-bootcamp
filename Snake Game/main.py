from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score_Board

score = 0
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game ")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score_Board()

# moving the snake automatically across the screen
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.turn_on_command()

    # detect collision with food
    if snake.segments[0].distance(food) < 20:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # detect collision with wall
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if (x_cor >= 300) or (x_cor <= -300):
        score_board.game_over()
        game_is_on = False
    elif (y_cor >= 300) or (y_cor <= -300):
        score_board.game_over()
        game_is_on = False

    # detect collision with tail
    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score_board.game_over()

screen.exitonclick()
