import turtle
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim = turtle.Turtle()
tim.speed(1)
tim.pensize(5)

for x in range(3, 10):
    tim.color(random_color())
    tim.forward(100)
    tim.right(360 / x)
    for y in range(0, x-1):
        tim.forward(100)
        tim.right(360 / x)

my_screen = turtle.Screen()
my_screen.exitonclick()
