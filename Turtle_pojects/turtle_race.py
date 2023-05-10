import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
y = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y[index])
    new_turtle.color(colors[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            winner=turtle.pencolor()
            is_race_on=False
            if winner==user_bet:
                print("Yay! You Won the Bet.")
                print(f"{winner} turtle won the race.")
            else:
                print(f"{winner} turtle won the race.")
                print("You lose")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



