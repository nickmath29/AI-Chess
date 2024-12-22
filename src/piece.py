
class Piece:
    
    def __init__(self, name, color, value, texture=None, teture_rect=None):
        pass
    
# Each class below represents a different piece: Pawn, Rook, Bishop, Knight, King, Queen

class Pawn(Piece):
    
    def __init__(self, color):
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
        super.__init__('pawn', color, 1.0)

class Knight(Piece):
    def __init__(self, color):
        super.__init__('knight', color, 3.0)
        
class Bishop(Piece):
    def __init__(self, color):
        super.__init__('bishop', color, 3.001) # We are putting more importance on Bishop than Knight

class Rook(Piece):
    def __init__(self, color):
        super.__init__('rook', color, 5.0)

class Queen(Piece):
    def __init__(self, color):
        super.__init__('queen', color, 9.0)
        
class King(Piece):
    def __init__(self, color):
        super.__init__('king', color, 10000.0)