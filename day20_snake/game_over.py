from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.teleport(x=0, y=0)
        self.hideturtle()
        self.color("white")
        self.game_over_write()

    def game_over_write(self):
        self.write("Game over", move=False, align='center', font=('Comic Sans MS', 25, 'normal'))
