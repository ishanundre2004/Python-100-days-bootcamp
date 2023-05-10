import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

t.listen()
t.onkey(key="w", fun=move_forward)
t.onkey(key="s", fun=move_backward)
t.onkey(key="d", fun=turn_right)
t.onkey(key="a", fun=turn_left)
t.onkey(key="c", fun=clear)

screen.exitonclick()