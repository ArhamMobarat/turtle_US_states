import pandas
import turtle as t
import time



data = pandas.read_csv("50_states.csv")
image = "blank_states_img.gif"
screen = t.Screen()
screen.addshape(image)
screen.setup(730,500)
t.shape(image)
screen.tracer(0)

state_list = data.state.to_list()
guessed_states = []
while len(guessed_states)<= 50:
    screen.update()
    time.sleep(0)
    user_input = screen.textinput(title=f"States {len(guessed_states)}/50 ", prompt="What's the next state? ").title()

    if user_input == "Exit":
        states_left = [state for state in state_list if state not in guessed_states]
        # for state in state_list:
        #     if state not in guessed_states:
        #         states_left.append(state)
        need_to_learn = pandas.DataFrame(states_left)
        need_to_learn.to_csv("States left to learn")
        break

    if user_input not in guessed_states:
        if user_input in state_list:
            guessed_states.append(user_input)
            state = t.Turtle()
            state.penup()
            state.hideturtle()
            state_data = data[data.state == user_input]
            state.goto(int(state_data.x),int(state_data.y))
            state.write(user_input)