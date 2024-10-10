from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
left_paddle = Paddle(-280)
right_paddle = Paddle(280)

left_score = 0
right_score = 0

left_scoreboard = ScoreBoard(-100, left_score)
right_scoreboard = ScoreBoard(100, right_score)


ball = Ball()
screen.tracer(0)
screen.setup(width=600, height=600, startx=0, starty=0)
screen.bgcolor("black")
screen.title("pong")

screen.listen()
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")

screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")


game = True
while game:
    ball.ball_mov()

    # collision with wall
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.ball_bonce_wall()

    # collision with paddle
    if ball.distance(left_paddle) <= 50 or ball.distance(right_paddle) <= 50:
        if ball.xcor() >= 270 or ball.xcor() <= -270:
            ball.ball_bonce_paddle()

    # out of bond/score
    if ball.xcor() >= 300:
        ball.ball_reset()
        left_score += 1
        print(f'left score = {left_score}')
        left_scoreboard.clear()
        left_scoreboard = ScoreBoard(-100, left_score)

    if ball.xcor() <= -300:
        ball.ball_reset()
        right_score += 1
        print(f'right score = {right_score}')
        right_scoreboard.clear()
        right_scoreboard = ScoreBoard(100, right_score)

    # game over
    def clear_scoreboard():
        left_scoreboard.clear()
        right_scoreboard.clear()
        ball.hideturtle()

    if left_score == 5:
        game_over = ScoreBoard(0, "left player won !")
        clear_scoreboard()
    if right_score == 5:
        game_over = ScoreBoard(0, "right player won !")
        clear_scoreboard()


    screen.update()


screen.exitonclick()
