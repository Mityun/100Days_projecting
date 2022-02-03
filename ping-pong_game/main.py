from turtle import Turtle, Screen
import time
from paddle_class import *

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong yeeeeah")
screen.tracer(0)

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)


screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_state_is_on = True
while game_state_is_on:
    time.sleep(0.02)
    screen.update()

screen.exitonclick()