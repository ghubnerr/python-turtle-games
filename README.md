# Python Turtle Graphics Turtle Race and Etch-a-Sketch!

## Using Event Listeners 
The *`turtle.listen`* methods (found in the 'Using Screen Events' section inside turtle documentation) allows the screen to wait for user's click and key strokes to perform actions. 

### Etch-a-Sketch
[`etch-a-sketch.py`](etch-a-sketch.py) listens for keys such as **'W', 'A', 'S', 'D'** to move Kevin<sup>[1]</sup> around. You can clear the screen and return the Kevin to its initial position by pressing 'C'.

## Object States and Instances in Python \

### Turtle Racing and Betting

[`turtle-race.py`](turtle-race.py) creates instances of the Turtle() objects at random colors, and whose object states are mutable according to preferences so one can, for example, change the color of a single turtle individually.
This allows a randomization in movement for the different states of the Turtle objects, creating a species of "unique race" for the turtles that move the fastest towards the right edge of the screen. The latter makes it crucial for the use of the method *`screen.setup(<width>, <height>`*, allowing the use of the *`turtle.goto(<x>,<y>)`* methods to set the initial position of the turtles.
Additionally, the function *`screen.textinput(<title>,<prompt>)`* creates a user prompt and returns the response in the form of a variable, which will be used to determine whether the user has bet on the winner turtle or not.


---
## Credits
The idea for these fun projects came from Dr. Angela Yu's 100 Days of Python Bootcamp for Udemy.

## License
This repository is licensed under the [MIT License](LICENSE).

--- 
<sup>[1]</sup>: Yes, I like to call turtles Kevin.