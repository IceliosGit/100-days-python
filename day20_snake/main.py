from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
from game_over import GameOver
import os.path


def restart():
    snake.restart()
    game_over.restart()
    score.reset()


def leave_game():
    global game_on  # I do it to avoid the error of leaving while in the loop. Would like to avoid global variable but
    # I did not find another way
    game_on = False


path = './save_score.txt'

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600, startx=0, starty=0)
screen.bgcolor("black")
screen.title("snake")

screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
game_over = GameOver()


screen.listen()
screen.onkey(snake.left_rotate, "a")
screen.onkey(snake.right_rotate, "d")
screen.onkey(leave_game, "Escape")

path = './save_score.txt'
game_on = True
while game_on:
    snake.move()
    # food and scored
    if os.path.isfile(path):  # check if there is already a game save, if yes, put highscore
        with open("save_score.txt", mode="r") as file:
            score.highscore_counter = int(file.read())
            print(score.highscore_counter)
        score.highscore_write()

    if snake.head.distance(food) < 15:  # check detection with food
        food.new_pos()
        snake.add_snake_part()
        score.score_counter += 1
        score.score_write()
        if score.score_counter >= score.highscore_counter:  # print new highscore
            score.highscore_counter = score.score_counter
        score.highscore_write()
        with open("save_score.txt", mode="w") as file:
            file.write(str(score.highscore_counter))
    screen.update()
    # wall
    if snake.head.ycor() > 280 or snake.head.ycor() < -280 \
            or snake.collision_with_tail() \
            or snake.head.xcor() > 280 or snake.head.xcor() < -280:
        screen.onkey(restart, "r")
        game_over.game_over_write()
        snake.stop_moving()
        screen.update()

quit()
