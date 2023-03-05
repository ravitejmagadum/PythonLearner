import turtle
import pandas
from name import Name

turtle.Turtle()
screen = turtle.Screen()
turtle.bgpic('blank_states_img.gif')
name = Name()
#
# answer_state = screen.textinput("Welcome to Quiz", "Name the state")
# states = pandas.read_csv("50_states.csv")
# # print(states['state'] == answer_state)
#
score = 0
while True:

    answer_state = screen.textinput(f"{score}/50 Welcome to Quiz", "Name the state")
    states = pandas.read_csv("50_states.csv")

    result = ~states['state'].isin([answer_state]).any()
    if result:
        continue

    else:
        cor = states[states['state'] == answer_state]
        xcor = cor.at[cor.index[0], 'x']
        ycor = cor.at[cor.index[0], 'y']
        name.goto_loc(x=xcor, y=ycor, answer_state=answer_state)
        score +=1



# print(axis['x'])
#
# x_cor = [axis['x'] == answer_state]
# #
# # x_cor, y_cor = axis['x'],  axis['y']
# print(x_cor)

# turtle.addshape('blank_states_img.gif')

turtle.mainloop()
