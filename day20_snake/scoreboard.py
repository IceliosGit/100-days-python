from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.teleport(x=-270, y=270)
        self.hideturtle()
        self.color("white")
        self.score_counter = 0
        self.score_write()

    def score_write(self):
        self.clear()
        self.write(f"score: {self.score_counter}", move=False, align='left', font=('Comic Sans MS', 12, 'normal'))
