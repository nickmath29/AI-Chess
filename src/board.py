from const import *
from square import Square

class Board:
    
    def __init__(self):
        self.squares = []
        
        self._create()
    
    def _create(self):
        self.squares = [[0,0,0,0,0,0,0,0] for cols in range(COLS)] # creating a 2d array
        
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] =  Square(row, col) # Adding a square object into that 2d array
    
    def _add_pieces(self, color):
        pass