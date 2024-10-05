from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=0.5, outline=None)
        self.goto(x=side, y=0)

    def paddle_up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)
