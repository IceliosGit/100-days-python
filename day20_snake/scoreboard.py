from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score_counter = 0
        self.highscore_counter = 0
        self.score_write()

    def score_write(self):
        self.goto(x=-270, y=270)
        self.clear()
        self.write(f"score: {self.score_counter}", move=False, align='left', font=('Comic Sans MS', 12, 'normal'))

    def highscore_write(self):
        self.goto(x=-200, y=270)
        self.write(f"highscore: {self.highscore_counter}", move=False, align='left', font=('Comic Sans MS', 12, 'normal'))

    def reset(self):
        self.score_counter = 0
        self.score_write()
        self.highscore_write()
