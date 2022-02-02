import time
from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My little Galgamesh. World' eater")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
blocks = []

for i in starting_positions:
    block = Turtle("square")
    block.penup()
    block.goto(i)
    block.color("white")

    blocks.append(block)

game_state_is_on = True

while game_state_is_on:
    screen.update()
    time.sleep(0.2)
    for seg_num in range(len(blocks) - 1, 0, -1):
        new_x = blocks[seg_num - 1].xcor()
        new_y = blocks[seg_num - 1].ycor()
        blocks[seg_num].goto(new_x, new_y)
    blocks[0].forward(20)


screen.exitonclick()