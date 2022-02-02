import time
from turtle import Screen, Turtle
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My little Galgamesh. World' eater")
screen.tracer(0)

game_state_is_on = True

snake = Snake()

screen.listen()

screen.onkey(snake.up(), 'w')
screen.onkey(snake.down(), 's')
screen.onkey(snake.left(), 'a')
screen.onkey(snake.right(), 'd')

while game_state_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()



screen.exitonclick()