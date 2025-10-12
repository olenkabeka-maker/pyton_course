"""Game mine sweeper.
Generate map, ask user to guess where mine is.
"""
import random

MAP_SIZE = 8
MINE_COUNT = MAP_SIZE
MAP = {}

# Print header coordinates
numbers_string = []
for number in list(range(1, MAP_SIZE+1)):
    numbers_string.append(str(number))
print('  ' + ''.join(numbers_string))


# Print map and line numbers
for i in range(MAP_SIZE):
    line = []
    for x in range(MAP_SIZE):
        line.append('O')
    print(i+1, ''.join(line))
    MAP[i] = line

# Generate mine coordinates
MINE_COORDINATE = {}
for line in range(0, MAP_SIZE):
    MINE_COORDINATE[line] = random.randint(0, MAP_SIZE)

TOTAL_CELLS = MAP_SIZE * MAP_SIZE
EMPTY_CELLS = TOTAL_CELLS - MAP_SIZE

FOUND_EMPTY_CELLS = 0

ERROR_MESSAGE_WRONG_FORMAT = 'Wrong input, format: "row col"'

while EMPTY_CELLS != FOUND_EMPTY_CELLS:
    guess = input('Enter coordinates to check > ')
    if len(guess) > 3:
        print(ERROR_MESSAGE_WRONG_FORMAT)
        continue
    if not guess[1] == ' ':
        print(ERROR_MESSAGE_WRONG_FORMAT)
        continue
    one, two = guess.split(' ')

    if one.isdigit() and two.isdigit():
        col = int(one)
        row = int(two)

    if (col > 0 and col < MAP_SIZE + 1) and (row > 0 and row < MAP_SIZE + 1):
        if MINE_COORDINATE[col] == row:
            print('This is a mine.')
            break
        else:
            MAP[row][col] = 'X'
            # Print map and line numbers
            for idx, line in MAP.items():
                print(idx+1, ''.join(line))