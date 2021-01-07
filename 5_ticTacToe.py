# A tic-tac-toe board looks like a large hash symbol (#) with nine slots that can each contain an X, an O, or a blank.
# To represent the board with a dictionary, you can assign each slot a string-value key.
# 'top-L', 'top-M', 'top-R'
# 'mid-L', 'mid-M', 'mid-R'
# 'low-L', 'low-M', 'low-R'

# You can use string values to represent what's in each slot on the board: 'X', 'O' or ''.
    # Thus, you'll need nine strings.
    # You can use a dictionary of values for this.
        # The string value with the key 'top-R' can represent the top right corner, the string value with with the key 'low-L' can represent the bottom-left corner and so on.

# Declares a dictionary
theBoard = {'top-L': '', 'top-M': '', 'top-R': '',
'mid-L': '', 'mid-M': '', 'mid-R': '',
'low-L': '', 'low-M': '', 'low-R': ''}

# Defines a function that prints the tic-tac-toe board
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

# Code that allows the players to enter their moves.

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
