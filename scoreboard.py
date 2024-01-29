from turtle import Turtle


class Scoreboard(Turtle):
    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.write_score()

    def l_scored(self):
        self.l_score += 1
        self.write_score()

    def r_scored(self):
        self.r_score += 1
        self.write_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game_Over", align="center", font=("Courier", 80, "normal"))
        self.goto(-100, -100)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, -100)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

