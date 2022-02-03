from turtle import Turtle
import random


class Food:
    def __init__(self):
        self.food_p = []
        self.create_food()
        self.x = self.food_p[-1].xcor()
        self.y = self.food_p[-1].ycor()

    def create_food(self):
        food = Turtle("circle")
        food.penup()
        food.goto(random.randint(-300, 300), random.randint(-300, 300))
        food.color("red")

        self.food_p.append(food)

    # def if_eaten(self, cur_x, cur_y):
    #     if cur_x == self.x and cur_y == self.y:
    #         return True
    #     return False
