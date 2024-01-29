from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.penup()
        self.goto(x=position_x, y=position_y)
        self.shape("square")
        self.color("white")
        self.resizemode('user')
        self.setheading(90)
        self.turtlesize(stretch_len=5, stretch_wid=1)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
