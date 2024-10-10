from turtle import Turtle
from random import random
from random import randint


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color(round(random(), 2), round(random(), 2), round(random(), 2))
        self.penup()
        self.goto(randint(-350, 350), randint(-200, 200))

    def car_moving(self, speed):
        self.setx(self.xcor() - speed)
        if self.xcor() < -350:
            self.setx(350)


