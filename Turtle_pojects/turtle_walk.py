import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions=[0, 90, 180, 270]
tim.pensize(15)
tim.speed(0)

for _ in range(500):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

my_screen = turtle.Screen()
my_screen.exitonclick()
