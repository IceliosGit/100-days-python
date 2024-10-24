import turtle
import pandas

screen = turtle.Screen()
screen.title("US_states_game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
number_guessed = 0

while number_guessed < 50:
    answer_state = screen.textinput(title=f"Guess the state  {number_guessed}/50", prompt="What's another state name?")
    answer_state = answer_state.title()  # Put the first letter in uppercase if not already the case
    # title() will put every single word with an uppercase first. capitalized will only do the first word
    if answer_state == "Exit":
        df = pandas.DataFrame(state_list)
        df.to_csv("List_of_missed_states.csv")
        break

    if answer_state in state_list:
        number_guessed += 1
        state_list.remove(answer_state)
        state_coor = data[data.state == answer_state]
        index = int(state_coor.index[0])  # Don't know why I have to do that, needed for below otherwise do not work

        # prof uses writer.goto(state_data.x.item(), state_data.y.item()) instead to avoid this problem
        writer.goto(state_coor.x[index], state_coor.y[index])
        writer.write(f"{answer_state}", align="center", font=("Arial", 8))
