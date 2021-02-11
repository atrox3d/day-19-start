from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
print(bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def create_turtles():
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtle.penup()
        turtles.append(turtle)


def position_turtles():
    yoffset = 50
    ystart = yoffset * 3
    xstart = -230

    for turtle in turtles:
        turtle.goto(x=xstart, y=ystart)
        ystart -= yoffset


create_turtles()
position_turtles()



# tim.penup()
# tim.goto(x=-230, y=-100)

screen.exitonclick()

