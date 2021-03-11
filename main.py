import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=500, height=650)
screen.title("Bangladesh Districts Game")
image = "map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("bangladesh_districts.csv")
all_districts = data.state.to_list()
guessed_states = []

while len(guessed_states) < 65:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/64 districts correct.",
                                    prompt="What's another District name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_districts if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_districts:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(answer_state, font=("Rockwell", 6, "normal"))

screen.exitonclick()
