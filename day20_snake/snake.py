from turtle import Turtle
from time import sleep

SNAKEPART_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.snake_creation(SNAKEPART_POS)
        self.head = self.snake[-1]
        self.allowed_to_move = True

    def set_move(self, val_bool):
        self.allowed_to_move = val_bool

    def snake_part_creation(self, order):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        self.snake.insert(order, snake_part)

    def snake_creation(self, position):
        for snake_pos in range(3):
            self.snake_part_creation(0)
            self.snake[snake_pos].goto(position[snake_pos])

    def add_snake_part(self):
        self.snake_part_creation(1)
        self.snake[1].goto(self.snake[2].pos())

    def left_rotate(self):
        self.snake[-1].left(90)

    def right_rotate(self):
        self.snake[-1].right(90)

    def move(self):
        sleep(0.1)
        for part in range(len(self.snake) - 1, 0, -1):  # len = 3-1, so 2, 1
            self.snake[-part - 1].goto(x=self.snake[-part].xcor(), y=self.snake[-part].ycor())
        self.snake[-1].forward(20)

    def collision_with_tail(self):
        for snake_part in self.snake:
            if self.head.distance(snake_part) < 15 and self.head != snake_part:
                return True

    def restart(self):
        for part in range(len(self.snake)):  # len = 3-1, so 2, 1
            self.snake[part].goto(1000, 1000)  # teleport the old
            # snake off_screen
        self.snake.clear()
        self.snake_creation(SNAKEPART_POS)
        self.head = self.snake[-1]