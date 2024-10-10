from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(0, -250)

    def move_forward(self):
        self.sety(self.ycor() + 20)

    def move_backward(self):
        self.sety(self.ycor() - 20)


