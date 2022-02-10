from turtle import *
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.x_rand_start = random.choice([-5, 5])
        self.y_rand_start = random.choice([-5, 5])
        self.x_move = self.x_rand_start
        self.y_move = self.y_rand_start

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
