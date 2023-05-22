from turtle import Turtle, Screen

FIXED_STEP = 10

kevin = Turtle()
screen = Screen()
kevin.shape("turtle")


def redefine_step(change: int) -> None:
    """Redefines globally the fixed step distance for every forward-key pressed"""
    global FIXED_STEP
    FIXED_STEP = change


def move_forward() -> None:
    """Moves forward the predefined step distance"""
    kevin.forward(FIXED_STEP)


def turn_right() -> None:
    """Turns 5 degrees to the right"""
    kevin.rt(5)


def turn_left() -> None:
    """Turns 5 degrees to the left"""
    kevin.lt(5)


def move_backwards() -> None:
    """Moves backwards a fixed amount without changing heading direction"""
    kevin.backward(FIXED_STEP)


def clear_screen() -> None:
    """Clears the screen and sends the turtle back to the middle"""
    kevin.clear()
    kevin.reset()
    

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
