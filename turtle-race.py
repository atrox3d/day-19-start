from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
print(bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def create_turtles():
    turtle : Turtle
    for current_color in range(len(colors)):
        turtle = Turtle(shape="turtle")
        turtle.color(colors[current_color])
        turtle.penup()
        turtles.append(turtle)


def position_turtles():
    yoffset = 50
    ystart = yoffset * 3
    xstart = -230
    turtle: Turtle
    for turtle in turtles:
        turtle.goto(x=xstart, y=ystart)
        ystart -= yoffset


create_turtles()
position_turtles()

race = True
t: Turtle
winner = None

while race:
    for t in turtles:
        t.forward(random.randint(0, 10))
        if t.xcor() >= 230:
            winner = t.pencolor()
            race = False

print(winner)

if winner == bet:
    print("you win!")
else:
    print("you lose")


# tim.penup()
# tim.goto(x=-230, y=-100)

screen.exitonclick()

