from turtle import Turtle, Screen

kevin = Turtle()
screen = Screen()
screen.listen()


# Using event listeners to bind a key-stroke: https://docs.python.org/3/library/turtle.html/turtle-listen

def move_forwards():
    """This makes the turtle run 10 paces -- a set distance"""
    kevin.forward(10)


# Higher order functions for event-listeners:
# It's important to use kwargs instead of positional arguments when using higher order functions!

screen.onkey(key="space", fun=move_forwards)  # Passing the function `move_forwards` as argument of `on_key` function.
screen.exitonclick()
