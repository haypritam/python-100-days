import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. States")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

aState=0
data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_statets=[]

while len(guessed_statets)<50:
    answer_state=screen.textinput(title="Guess the state", prompt="whats anothers state's name?")
    if answer_state=="Exit":
        missing_state=[]
        for state in all_states:
            if state not in guessed_statets:
                missing_state.append(state)
        new_data=pandas.DataFrame( missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_statets.append(answer_state)
        t = turtle.Turtle()
        t.ht()
        t.pu()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

