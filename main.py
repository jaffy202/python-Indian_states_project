import turtle
import enter as e
import pandas as pd

screen = turtle.Screen()
entry = e.Entry()
screen.title("Indian States Game")

image = "india.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("states.csv")
data = df
states = df.state
states_list = states.to_list()
guessed_states = []
no_of_correct_answers = 0
no_of_guessed_states = len(guessed_states)

while no_of_guessed_states < 33:
    answer_state = screen.textinput(title=f"{no_of_correct_answers}/33 states correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        data["state"].to_csv("learnStates.csv")
        break
    if answer_state not in guessed_states:
        if answer_state in states_list:
            no_of_correct_answers += 1
            guessed_states.append(answer_state)
            line_no = df[df.state == answer_state].index[0]
            data = data.drop(line_no)
            entry.write_place(answer_state, df["x"][line_no], df["y"][line_no])
