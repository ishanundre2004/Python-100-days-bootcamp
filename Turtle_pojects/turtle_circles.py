import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for angle in range(360):
    tim.color(random_color())
    tim.circle(100)
    if angle%5==0:
        tim.setheading(angle)

my_screen = turtle.Screen()
my_screen.exitonclick()
