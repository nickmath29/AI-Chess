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
        
        def pawn_moves():
            # Alternate verison below: steps = 1 if piece.moved else 2
            if piece.moved:
                steps = 1
            else:
                steps = 2
            
            # Vertical Moves
            start = row + piece.dir
            end = row + (piece.dir * (1 + steps))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        # create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        #create new move
                        move = Move(initial, final)
                        # append a move
                        piece.add_move(move)
                    else:
                        break
                else:
                    break
                
            # Diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col-1, col+1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                        # create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        #create new move
                        move = Move(initial, final)
                        # append a move
                        piece.add_move(move)                     
             
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
                        
        def strightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr
                
                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        # empty
                        
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create a possible new move
                        move = Move(initial, final)
                        
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            # append new move  
                            piece.add_move(move)    
                        
                        # has enemy
                        if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                            # append new move
                            piece.add_move(move)
                            break
                        
                        # has team piece so break
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break
                        
                    else: break
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr
         
        def king_moves():
            adj = [
                (row - 1, col + 0), # Up
                (row - 1, col + 1), # Up-Right
                (row + 0, col + 1), # Right
                (row + 1, col + 1), # Down-Right
                (row + 1, col + 0), # Down
                (row + 1, col - 1), # Down-Left
                (row + 0, col - 1), # Left
                (row - 1, col - 1)  # Up-Left
            ]
            
            # normal moves
            for possible_move in adj:
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
            
            # queen castling
            
            # king castling
                        
        if isinstance(piece, Pawn):
            pawn_moves()
            
        elif isinstance(piece, Knight):
            knight_moves()
            
        elif isinstance(piece, Bishop):
            strightline_moves([
                (-1, +1), # up-right
                (-1, -1), # up-left 
                (1, 1),   # down-right
                (1, -1)   # down-left
            ])
            
        elif isinstance(piece, Rook):
            strightline_moves([
                (-1, 0), # up
                (0, 1),  # right
                (1, 0),  # down
                (0, -1)  # left
            ])
        elif isinstance(piece, Queen):
             strightline_moves([
                (-1, +1), # up-right
                (-1, -1), # up-left 
                (1, 1),   # down-right
                (1, -1),   # down-left
                (-1, 0), # up
                (0, 1),  # right
                (1, 0),  # down
                (0, -1)  # left
             ])
        elif isinstance(piece, King):
            king_moves()       
        
        
        
    
    
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
