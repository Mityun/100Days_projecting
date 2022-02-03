from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        self.x_cor = x_cor
        self.y_cor = y_cor
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.color("white")
        self.goto(self.x_cor, self.y_cor)

    def up(self):
        if self.y_cor <= 270:
            self.y_cor += 20
            self.goto(self.x_cor, self.y_cor)

    def down(self):
        if self.y_cor >= -270:
            self.y_cor -= 20
            self.goto(self.x_cor, self.y_cor)
