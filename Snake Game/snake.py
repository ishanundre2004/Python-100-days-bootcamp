from turtle import Turtle
import turtle as t

starting_position = [(-40, 0), (-20, 0), (0, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(20)

    def turn_east(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_north(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_west(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_south(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_on_command(self):
        t.listen()
        t.onkey(self.turn_east, "Right")
        t.onkey(self.turn_north, "Up")
        t.onkey(self.turn_west, "Left")
        t.onkey(self.turn_south, "Down")
