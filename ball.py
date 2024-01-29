from turtle import Turtle

BALL_SPEED = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(45)
        self.move_speed = BALL_SPEED

    def speed_up(self):
        self.move_speed *= 0.9

    def move(self):
        self.forward(10)

    def bounce(self):
        head = self.heading() - 90
        self.setheading(head)

    def reset(self):
        self.goto(0, 0)
        self.move_speed = BALL_SPEED
        self.bounce()
