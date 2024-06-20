import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game')
image = 'D:\\Python\\US States Game\\blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
states_guessed = []
states_forgotten = []
count = 0
state_file = pandas.read_csv('D:\\Python\\US States Game\\50_states.csv')
state_names = state_file.state
print(state_names)

while count < 50:
    answer = screen.textinput(title='Guess a State', prompt='Type the state name here')

    if answer.lower() == 'exit':
        break
    for state_ in state_names:

        if answer.lower() == state_.lower():
            count += 1
            name_turtle = turtle.Turtle()
            name_turtle.penup()
            name_turtle.hideturtle()
            name_turtle.goto(int(state_file[state_file['state'] == state_].x), int(state_file[state_file['state'] == state_].y))
            name_turtle.write(state_)
            states_guessed.append(state_)


states_forgotten = [state for state in state_names if state not in states_guessed]
new_file_dic = {
    'state': states_forgotten
}

states_to_learn = pandas.DataFrame(new_file_dic)
states_to_learn.to_csv('states to learn')


turtle.mainloop()
