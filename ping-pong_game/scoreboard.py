from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.__l_score = 0
        self.__r_score = 0
        self.goto(-100, 200)
        self.update_score()

    def l_point(self):
        self.__l_score += 1
        self.update_score()

    def r_point(self):
        self.__r_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.__l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.__r_score, align="center", font=("Courier", 80, "normal"))