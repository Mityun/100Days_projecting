import time
from turtle import Screen, Turtle
from snake import Snake
import random
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My little Galgamesh. World' eater")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_state_is_on = True
food = Turtle("circle")
food.penup()
food.goto(random.randint(-300, 300), random.randint(-300, 300))
food.color("red")


while game_state_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.xcor() >= 298 or snake.head.xcor() <= -298 or snake.head.ycor() >= 298 or snake.head.ycor() <= -298:
        # check on going out of bounds
        game_state_is_on = False

    if snake.head.distance(food.xcor(), food.ycor()) <= 20:  # condition for eating food
        snake.add_segment()
        food.goto(random.randint(-250, 250), random.randint(-250, 250))
    for i in snake.segments[1:]:
        if snake.head.pos() == i.pos():
            game_state_is_on = False


screen.exitonclick()

# TODO: scoreboard
