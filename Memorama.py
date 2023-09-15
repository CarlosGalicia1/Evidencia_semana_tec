"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *
from freegames import path

# Load the car image (for the background).
car = path('car.gif')

# Create a list of 32 pairs of numbers from 0 to 31 to represent the game tiles.
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0  # Variable to count taps, initialized to 0

# Function to draw a square at the position (x, y).
def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Function to convert coordinates (x, y) into a tile index.
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Function to convert a tile index into coordinates (x, y).
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Function to update and display the tap count.
def update_tap_count():
    up()
    goto(160, -190)
    color('black')
    write(f'Taps: {tap_count}', align='center', font=('Arial', 16, 'normal'))

# Function to handle the click event on a tile.
def tap(x, y):
    global tap_count
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        tap_count += 1
        update_tap_count()

# Function to draw the car image and the game tiles.
def draw():
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update_tap_count()  # Update the counter in each frame
    update()
    ontimer(draw, 100)

shuffle(tiles)

# Set up the game and draw the initial interface.
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
