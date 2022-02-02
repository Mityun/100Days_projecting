from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    '''
    class for creating a snake body and add sections to it's body
    '''
    def __init__(self):
        self.segments = []  # all positions of segments
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            block = Turtle("square")
            block.penup()
            block.goto(i)
            block.color("white")

            self.segments.append(block)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # this block make each previous segment take position of a
            new_x = self.segments[seg_num - 1].xcor()  # segment in front of him.
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)






