from turtle import Turtle
from time import sleep

SNAKEPART_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.snake_creation(SNAKEPART_POS)
        self.head = self.snake[-1]

    def snake_part_creation(self, order):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        self.snake.insert(order, snake_part)

    def snake_creation(self, position):
        for snake_pos in range(3):
            self.snake_part_creation(0)
            self.snake[snake_pos].goto(position[snake_pos])  # teleport does not work with tuple :/

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
            self.snake[-part - 1].teleport(x=self.snake[-part].xcor(), y=self.snake[-part].ycor())
        self.snake[-1].forward(20)

    def collision_with_tail(self):
        for snake_part in self.snake:
            if self.head.distance(snake_part) < 15 and self.head != snake_part:
                return True
