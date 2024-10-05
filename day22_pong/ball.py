from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_mov = 0.1
        self.y_mov = 0.1
        self.ball_reset()

    def acceleration(self):
        self.x_mov *= 1.5
        self.y_mov *= 1.5

    def ball_mov(self):
        new_x = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov
        self.goto(new_x, new_y)

    def ball_bonce_wall(self):
        self.y_mov = -self.y_mov
        self.acceleration()

    def ball_bonce_paddle(self):
        self.x_mov = -self.x_mov
        self.acceleration()

    def ball_reset(self):
        self.goto(x=0, y=randint(-250, 250))
        self.x_mov = 0.1
        self.y_mov = 0.1
        if randint(0, 1) == 0:
            self.x_mov *= -1
        if randint(0, 1) == 0:
            self.y_mov *= -1


