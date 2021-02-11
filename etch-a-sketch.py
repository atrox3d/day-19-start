from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


FORWARDS = "w"
BACKWARDS = "s"
CLOCKWISE = "d"
COUNTERCLOCKWISE = "a"
CLEAR = "c"


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clockwise():
    tim.setheading(tim.heading() + 10)


def counterclockwise():
    tim.setheading(tim.heading() - 10)


def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()


screen.listen()
screen.onkey(key=FORWARDS, fun=move_forward)
screen.onkey(key=BACKWARDS, fun=move_backward)
screen.onkey(key=CLOCKWISE, fun=clockwise)
screen.onkey(key=COUNTERCLOCKWISE, fun=counterclockwise)
screen.onkey(key=CLEAR, fun=clear)

screen.exitonclick()

