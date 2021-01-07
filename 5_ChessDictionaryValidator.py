# Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.
# A valid board will have exactly one black king and exactly one white king.
# Each player can only have at most 16 pieces, at most 8 pawns.
# All pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'.
# The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
# This function should detect when a bug has resulted in an improper chess board.

chessBoard = {'1a':'wrook', '1b':'wknight', '1c':'wbishop', '1d':'wqueen', '1e':'wking', '1f':'wbishop', '1g':'wknight', '1h':'wrook',
                           '2a':'wpawn', '2b':'wpawn', '2c':'wpawn', '2d':'wpawn', '2e':'wpawn', '2f':'wpawn', '2g':'wpawn', '2h':'wpawn',
                           '3a':' ', '3b':' ', '3c':' ', '3d':' ', '3e':' ', '3f':' ', '3g':' ', '3h':' ',
                           '5a':' ', '5b':' ', '5c':' ', '5d':' ', '5e':' ', '5f':' ', '5g':' ', '5h':' ',
                           '6a':' ', '6b':' ', '6c':' ', '6d':' ', '6e':' ', '6f':' ', '6g':' ', '6h':' ',
                           '7a':'bpawn', '7b':'bpawn', '7c':'bpawn', '7d':'bpawn', '7e':'bpawn', '7f':'bpawn', '7g':'bpawn', '7h':'bpawn',
                           '8a':'brook', '8b':'bknight', '8c':'bbishop', '8d':'bqueen', '8e':'bking', '8f':'bbishop', '8g':'bknight', '8h':'brook'}


def isValidChessBoard(chessBoard):
    piecesCount = {'b': 0, 'w': 0}
    pawnCount = {'b': 0, 'w': 0}
    hasKing = {'b': False, 'w': False}
    letterAxis = ('a','b','c','d','e','f','g','h')
    pieceColor = ('b','w')
    pieceType = ('pawn','knight','bishop','rook','queen','king')

    for pos, piece in chessBoard.items(): # pos is the key(square positions). piece is the value (piece types)
        if int(pos[0]) >= 9: # This will check if position is between 1 to 8.
            print('Position error: Position must be between 1 to 8.')
        if (pos[1]) not in letterAxis: # This will check if space is valid = between a to h.
            print('Space Error: Spaces must be between a to h.')

        if piece[0] != ' ':
            if piece[0] not in pieceColor: # If first letter of piece is not w or b, an error will be returned.
                print('Color Error: Pieces must be White or Black.')

            thisPieceColor = piece[0] # The first letter of piece is either w or b. We'll use that as the key on piecesCount list.
            piecesCount[thisPieceColor] += 1 # Counter for piecesCount[w] and piecesCount[b]

            if piecesCount[thisPieceColor] >= 17: # An error is returned if either of the white or black piece counts exceed 16.
                print('TotalPieceError')


            thisPieceType = piece[1:] # This portion will check for piece types: king, queen, rook, bishop, knight, pawn
            if thisPieceType not in pieceType: # Error will be returned if not king, queen, rook, bishop, knight, pawn
                print('Incorrect piece.')

            elif thisPieceType == 'pawn': # Pawns will be counted
                pawnCount[thisPieceColor] += 1

                if pawnCount[thisPieceColor] >= 9: # Error will be returned if pawn count exceeds 8.
                    print('Incorrect number of pawns.')

            elif thisPieceType == 'king': # For kings, refer to line 20: hasKing = {'b': False, 'w': False}
                if hasKing[thisPieceColor] == True: # If hasKing[b] or hasKing[w] is already True, then previous iterations detected a King already.
                    print('Error: Already has king.') # Error will be returned.

                hasKing[thisPieceColor] = True # This will change value of hasKing[b] or hasKing[w] from False to True.

    if list(hasKing.values()) != [True, True]: # If the iterations have already finished but hasKing values are not yet True, True, then a king or 2 kings is missing.
        print('Error: Missing King.') # Error will be printed.

    return 'This board checks out.'





print(isValidChessBoard(chessBoard))
