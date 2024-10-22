import turtle
import pandas

screen = turtle.Screen()
screen.title("US_states_game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?")
print(answer_state.capitalize())  # Put the first letter in uppercase if not already the case

data = pandas.read_csv("50_states.csv")
state_name = data["state"]
print(state_name)




screen.exitonclick()
