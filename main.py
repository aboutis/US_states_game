import turtle
import pandas as pd
from turtlego import Writing


data = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("US States Game")
background = "blank_states_img.gif"
turtle.addshape(background)
turtle.shape(background)
commands = Writing()
score = 0
states = []
game = True
while game:
    answer_state = screen.textinput(title="Guess the state", prompt="Name a state: ")
    if answer_state in data.values:
        states.append(answer_state)
        score += 1
        index = data.index[data.state == answer_state].tolist()
        for i in index:
            x = data._get_value(i, "x")
            y = data._get_value(i, "y")
        commands.go(x, y)
        commands.writ(answer_state)
    else:
        commands.clear()
        commands.game_over(score)
        screen.exitonclick()
        game = False
