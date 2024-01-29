from turtle import Turtle, Screen
from time import sleep

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

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
ball = Ball()
scoreboard = Scoreboard()

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


def game_over():
    global game_is_on
    scoreboard.game_over()
    game_is_on = False
    screen.update()


screen.onkeypress(
    game_over,
    'q'
)
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -330 or (ball.distance(paddle) < 50 and ball.xcor() > 330):
        ball.bounce()
        ball.speed_up()
    if ball.xcor() > 380:
        scoreboard.l_scored()
        ball.reset()
    if ball.xcor() < -380:
        scoreboard.r_scored()
        ball.reset()

screen.exitonclick()
