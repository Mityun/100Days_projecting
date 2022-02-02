from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    '''
    class for creating a snake body and add sections to it's body
    '''
    def __init__(self):
        self.segments = []  # all positions of segments
        self.create_snake()
        self.head = self.segments[0]
        self.last_segment_position = self.segments[-1]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.goto(i)
            segment.color("white")

            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # this block make each previous segment take position of a
            new_x = self.segments[seg_num - 1].xcor()  # segment in front of him.
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        last_x = self.last_segment_position.xcor()
        last_y = self.last_segment_position.ycor()

        if self.head.heading() == UP:
            segment.goto(last_x, last_y - 20)
        if self.head.heading() == DOWN:
            segment.goto(last_x, last_y + 20)
        if self.head.heading() == LEFT:
            segment.goto(last_x + 20, last_y)
        if self.head.heading() == RIGHT:
            segment.goto(last_x - 20, last_y)

        self.segments.append(segment)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)






