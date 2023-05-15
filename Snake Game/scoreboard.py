from turtle import Turtle


class Score_Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 267)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"Score = {self.score}", align="center", font=('courier', 20, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=('courier', 24, 'bold'))
        self.hideturtle()
