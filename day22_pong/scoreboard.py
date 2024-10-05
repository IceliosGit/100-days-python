from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, side, score):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(side, 200)
        self.color("white")
        self.write(score, align="center", font=('Comic Sans MS', 35, 'normal'))


