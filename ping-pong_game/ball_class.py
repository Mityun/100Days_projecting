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
        self.__move_speed = 0.1

    def get_move_speed(self):
        return self.__move_speed


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.__move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.__move_speed = 0.01
        self.bounce_x()

