from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.setup(width=1920, height=1080, startx=0, starty=0)
turtle.shape("turtle")


def for_10():
    turtle.forward(10)


def bck_10():
    turtle.backward(10)


def left_rotate():
    turtle.left(36)


def right_rotate():
    turtle.right(36)


def reset():
    turtle.clear()
    turtle.home()


screen.listen()
screen.onkey(for_10, "w")
screen.onkey(bck_10, "s")
screen.onkey(left_rotate, "a")
screen.onkey(right_rotate, "d")
screen.onkey(reset, "c")


screen.mainloop()
