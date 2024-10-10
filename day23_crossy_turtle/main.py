from turtle import Screen
from player import Player
from cars import Car
from random import randint
from scoreboard import Scoreboard

screen = Screen()
player = Player()
scoreboard = Scoreboard()
cars = []

lvl = 1
scoreboard.level(lvl)
# Create multiple cars
for n_car in range(20):
    car = Car()  # Create a new car instance
    retry = True
    while retry:
        car_pos = randint(-350, 350), randint(-200, 200)  # Adjust bounds to fit the screen
        car.goto(car_pos)

        # Check if the new car is too close to any existing cars
        if all(car.distance(existing_car) > 90 for existing_car in cars):  # avoid collision using all() function
            # existing_car is just the name for every item in cars, could be anything
            cars.append(car)  # Only add if it's a valid position
            retry = False

screen.tracer(0)  # Turn turtle animation off
screen.setup(width=600, height=600, startx=0, starty=0)
screen.bgcolor("white")  # does nothing, default setting

screen.listen()
screen.onkeypress(player.move_forward, key="w")  # Do not put () after the fun move_forward !!
screen.onkeypress(player.move_backward, key="s")
screen.onkeypress(screen.bye, key="Escape")


game_is_on = True
car_speed = 0.5


while game_is_on:
    # car movement
    for every_car in cars:
        every_car.car_moving(car_speed)
        # collision with car
    if any(player.distance(existing_car) < 25 for existing_car in cars):  # Any is like all but only one is necessary
        game_is_on = False
        scoreboard.game_over()
    # level management
    if player.ycor() > 250:
        player.sety(-250)
        lvl += 1
        scoreboard.level(lvl)
        car_speed += 0.15
    screen.update()

screen.exitonclick()






