from const import *
from square import Square
from piece import *
from move import Move

class Board:
    
    def __init__(self):
        self.squares = []
        
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
    
    
    def calc_move(self, piece, row, col):
        '''
            Calculate all the possible (valid) moves of a piece in a specific position
        '''
        
        def knight_moves():
            
            # A knight at most can have 8 possible moves
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create squares for new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # piece = piece
                        # create new move
                        move = Move(initial, final)
                        #append new valid move
                        piece.add_move(move)
                        
        
        
        if isinstance(piece, Pawn):
            pass
        elif isinstance(piece, Knight):
            knight_moves()
            
        elif isinstance(piece, Bishop):
            pass
        elif isinstance(piece, Rook):
            pass
        elif isinstance(piece, Queen):
            pass
        elif isinstance(piece, King):
            pass        
        
        
        pass
    
    
    def _create(self):
        self.squares = [[0,0,0,0,0,0,0,0] for cols in range(COLS)] # creating a 2d array
        
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] =  Square(row, col) # Adding a square object into that 2d array
    
    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
        
        #pawn
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
            
        #knight
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        
        #bishop
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        
        #Rook
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        
        #Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        
        #King
        self.squares[row_other][4] = Square(row_other, 4, King(color))
