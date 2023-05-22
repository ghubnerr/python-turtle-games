from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()

screen.setup(height=300, width=500)

race_on = False
user_bet = screen.textinput(title="Bet", prompt="Who do you think will be the winning Kevin (turtle)? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


# Creating the turtle (kevin)

y_position = -150
x_position = -220

kevins = []


def draw_finish_line():
    """Creates an invisible turtle object that draws a line on the screen to represent the finish line"""
    pen = Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(x=220, y=-130)
    pen.pendown()
    pen.lt(90)
    pen.forward(240)


for turtle_index in range(6):
    kevin = Turtle(shape="turtle")  # Shape initializer
    kevin.color(colors[turtle_index])
    kevin.penup()
    y_position += 40
    kevin.goto(x=x_position, y=y_position)
    kevins.append(kevin)

if user_bet:
    race_on = True
    draw_finish_line()

winner = ''
while race_on:
    for kevin in kevins:
        random_distance = randint(0, 10)
        kevin.forward(random_distance)
        if kevin.xcor() > 220 - 40/2:
            winner = kevin.color()[0]
            race_on = False

if user_bet.lower() == winner.lower():
    print("Congratulations, your kevin has won!")
else:
    print(f"You lose, the winning turtle was {winner.capitalize()} kevin!")


screen.exitonclick()
