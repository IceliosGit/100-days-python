from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
from game_over import GameOver

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600, startx=0, starty=0)
screen.bgcolor("black")
screen.title("snake")

screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.left_rotate, "a")
screen.onkey(snake.right_rotate, "d")

game_on = True
while game_on:
    snake.move()
    # food and scored
    if snake.head.distance(food) < 13:
        food.new_pos()
        snake.add_snake_part()
        score.score_counter += 1
        score.score_write()
    screen.update()
    # wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        break
    if snake.head.ycor() > 280 or snake.head.ycor() < -280:
        break
    if snake.collision_with_tail():
        break

GameOver()

screen.exitonclick()
