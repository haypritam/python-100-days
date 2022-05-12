import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. States")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state=screen.textinput(title="Guess the state", prompt="whats anothers state's name?")


