import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        self.goto(x, y)
        self.recoup()

    def recoup(self):
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        self.goto(x, y)
