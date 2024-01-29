from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(45)

    def move(self):
        self.forward(10)

    def bounce(self):
        head = self.heading() - 90
        self.setheading(head)

    def reset(self):
        self.goto(0, 0)
        self.bounce()
