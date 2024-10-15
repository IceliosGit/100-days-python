from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")

    def game_over_write(self):
        self.goto(x=0, y=100)
        self.write("Game over", move=False, align='center', font=('Comic Sans MS', 25, 'normal'))
        self.goto(x=0, y=-100)
        self.write("To restart, press 'r'", move=False, align='center', font=('Comic Sans MS', 20, 'normal'))

    def restart(self):
        self.clear()

