from turtle import Turtle

NUM_OF_SEC = 0


class Scoreboard(Turtle):
    def __init__(self, num_of_sec):
        global NUM_OF_SEC
        super().__init__()
        self.shape()
        self.hideturtle()
        self.penup()
        self.color("green")
        self.goto(0, 250)
        if num_of_sec != NUM_OF_SEC:
            self.write(f"score: {num_of_sec}", False, "center", ("Arial", 24, "normal"))
            NUM_OF_SEC = num_of_sec

#  TODO make scoreboard show only one lawyer
