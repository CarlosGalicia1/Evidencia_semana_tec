"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""
# Import the libraries
from turtle import *

from freegames import line

# Draw the lines of the cat
def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

# Draw the x
def drawx(x, y):
    """Draw X player."""
    line(x, y, x + 100, y + 100)
    line(x, y + 100, x + 100, y)

#Draw the o
def drawo(x, y):
    """Draw O player."""
    up()
    goto(x + 67, y + 5)
    down()
    circle(42)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 150) * 150 - 200


state = {'player': 0, 'board': [[None, None, None], [None, None, None], [None, None, None]]}
players = [drawx, drawo]

# Begins the game and the players, depending on each one, put x or o 
def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']

    if state['board'][int((y + 200) // 133)][int((x + 200) // 133)] is None:
        draw = players[player]
        draw(x, y)
        update()
        state['board'][int((y + 200) // 133)][int((x + 200) // 133)] = player
        state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()