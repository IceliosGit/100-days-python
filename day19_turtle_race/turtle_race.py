from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=500, startx=0, starty=0)

race_state = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will "
                                                          "win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
position = [-125, -75, -25, 25, 75, 125]
all_turtle = []

if user_bet:
    race_state = True

for r in range(6):
    turtle = Turtle()
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(colors[r])
    turtle.goto(x=-230, y=position[r])
    all_turtle.append(turtle)

while race_state:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            wining_color = turtle.color()
            if wining_color[0] == user_bet:
                print("You won!")
            else:
                print("You lost!")
            race_state = False
        else:
            random_mov = randint(0, 10)
            turtle.forward(random_mov)




screen.mainloop()
