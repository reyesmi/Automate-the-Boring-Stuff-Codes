# This program will rotate clockwise 90 degrees the input.
import copy
WIDTH = 9
HEIGHT = 6
grid = [['.', '.', '.', '.', '.', '.'], # This is the input that will be rotated 90 degrees.
        ['.', 'O', 'O', '.', '.', '.'], # This is a list of lists.
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
# 1. Copy the previous grid value.
nextCells = copy.deepcopy(grid)
# 2. Print the rotated version of the input.
while True: # Main program loop
    for y in range(HEIGHT): # Loop will iterate through the y values instead of the x values.
        for x in range (WIDTH):
            print (nextCells[x][y], end = ' ')
        print()
