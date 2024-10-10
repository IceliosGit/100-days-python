from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.color("black")

    def level(self, x_level):
        self.clear()
        self.goto(-240, 250)
        self.write(f'Level {x_level}', align="center", font=('Verdana', 20, 'normal'))

    def game_over(self):
        self.goto(25, 200)
        self.write("Game Over", align="center", font=("Comic Sans MS", 55, "normal"))
        self.goto(25, -250)
        self.write("Click anywhere to leave the game", align="center", font=("Comic Sans MS", 20, "normal"))


