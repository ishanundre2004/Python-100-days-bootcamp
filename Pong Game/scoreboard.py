from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.left_score, font=("Courier", 60, "bold"))
        self.goto(100, 200)
        self.write(arg=self.right_score, font=("Courier", 60, "bold"))

    def l_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.right_score += 1
        self.update_scoreboard()
