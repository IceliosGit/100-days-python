from turtle import Turtle
from turtle import Screen

turtle = Turtle()
turtle2 = Turtle()
screen = Screen()
screen.setup(width=600, height=600, startx=0, starty=0)

turtle.forward(20)
turtle2.goto(turtle.pos())  # Fuuuuuuuuuuu
turtle.forward(-20)

# what happen when turtle3 = turtle2 ?
screen.exitonclick()

