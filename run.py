# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
'''

1. User comes to app and greeted by welcome message then instructions on how to play the game
2. App then prints out the board. The board will always show relevant game information. 
  - Where user and computer are, where snakes and ladders are, whose turn it is and what they have rolled.
3. User always goes first
  - Prompt is then executed to inform the user to press enter to roll the die
  - App rolls die and moves their piece to the CURRENT_LOCATION + die_roll. If they land on
    a snake or ladder, they get moved up or down accordingly.
  - Computer goes next
4. When either user or computer get to >= 36, they win, user is then greeted with a message if won or lost.
5. Game is cleared in order to play again.

'''


BOARD_NUM_COLUMNS = 6
BOARD_NUM_ROWS = 6
LAST_BOARD_TILE = BOARD_NUM_COLUMNS * BOARD_NUM_ROWS

USER_POSITION = "U"
COMPUTER_POSITION = "C"
LADDER_POSITION = "L"
SNAKE_POSITION = "S"

SNAKES = {
    11: 2,
    21: 9,
    35: 22,
}

LADDERS = {
    1: 15,
    9: 19,
    23: 34,
}

def main():

def die_roll():

def print_instructions():

