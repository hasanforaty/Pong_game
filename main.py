from turtle import Turtle, Screen
from paddle import Paddle

# Setup Screen
screen = Screen()
screen.setup(
    width=800,
    height=600,
)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle(position_x=350, position_y=0)
left_paddle = Paddle(position_x=-350, position_y=0)
screen.listen()
screen.onkeypress(
    fun=left_paddle.move_up,
    key='w'
)
screen.onkeypress(
    fun=left_paddle.move_down,
    key='s'
)
screen.onkeypress(
    paddle.move_up,
    'Up'
)
screen.onkeypress(
    paddle.move_down,
    'Down'
)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
