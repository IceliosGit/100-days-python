from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.penup()
        self.teleport(x=randint(-280, 280), y=randint(-280, 280))

    def new_pos(self):
        self.teleport(x=randint(-280, 280), y=randint(-280, 280))
