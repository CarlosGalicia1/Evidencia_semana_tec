"""Memory, puzzle game.
Exercises:
1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

import random
import turtle
from freegames import path

# Load the car image (for the background).
car = path('car.gif')

# Create a list of 32 pairs of numbers from 0 to 31 to represent the game tiles.
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0  # Variable to count taps, initialized to 0
uncovered_tiles = 0  # Variable to count uncovered tiles, initialized to 0

# Function to draw a square at the position (x, y).
def square(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

# Function to convert coordinates (x, y) into a tile index.
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Function to convert a tile index into coordinates (x, y).
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Function to update and display the tap count.
def update_tap_count():
    turtle.up()
    turtle.goto(160, -190)
    turtle.color('black')
    turtle.write(f'Taps: {tap_count}', align='center', font=('Arial', 16, 'normal'))

# Function to check if all tiles have been uncovered and display a win message.
def check_game_over():
    if uncovered_tiles == len(tiles):
        turtle.up()
        turtle.goto(0, 0)
        turtle.color('black')
        turtle.write('You win!', align='center', font=('Arial', 30, 'normal'))

# Function to handle the click event on a tile.
def tap(x, y):
    global tap_count, uncovered_tiles
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
        uncovered_tiles += 2  # Increment the uncovered tiles for each matching pair
        check_game_over()  # Check if all tiles have been uncovered after each valid tap

# Function to draw the car image and the game tiles.
def draw():
    turtle.clear()
    turtle.goto(0, 0)
    turtle.shape(car)
    turtle.stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        turtle.up()
        turtle.goto(x + 2, y)
        turtle.color('black')
        turtle.write(tiles[mark], font=('Arial', 30, 'normal'))

    update_tap_count()  # Update the tap count display in each frame
    turtle.update()
    turtle.ontimer(draw, 100)

random.shuffle(tiles)

# Set up the game and draw the initial interface.
turtle.setup(420, 420, 370, 0)
turtle.addshape(car)
turtle.hideturtle()
turtle.tracer(False)
turtle.onscreenclick(tap)
draw()
turtle.done()
