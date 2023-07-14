from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update_score(self):
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("arial", 75, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("arial", 75, "normal"))

    def l_scores(self):
        self.clear()
        self.l_score += 1

    def r_scores(self):
        self.clear()
        self.r_score += 1