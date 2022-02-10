from turtle import Turtle, Screen
import time
from paddle_class import *
from ball_class import *


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong yeeeeah")
screen.tracer(0)

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
ball = Ball()


screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_state_is_on = True
while game_state_is_on:
    time.sleep(0.02)
    screen.update()
    ball.move()

    # detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with the right paddle
    if ball.distance(paddle_r) < 60 and ball.xcor() > 330 or ball.distance(paddle_l) <= 60 and ball.xcor() < -330:
        ball.bounce_x()

    # ball hit right or left part of screen = sbd lost
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.color("black")
        screen.update()
        time.sleep(3)
        ball = Ball()

screen.exitonclick()