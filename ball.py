from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.penup()
        ran_angle = [random.randint(-40, 40), random.randint(140, 230)]
        self.setheading(random.choice(ran_angle))

    def move(self):
        if not (-245 < self.ycor() < 245):
            self.setheading(-self.heading())
        self.fd(8)

    def refresh(self):
        self.goto(0, 0)
        ran_angle = [random.randint(-40, 40), random.randint(140, 230)]
        self.setheading(random.choice(ran_angle))
