import pygame

from const import *
from board import Board
from dragger import Dragger
from square import Square


class Game:
    
    def __init__(self):
        self.next_player = 'white'
        self.board = Board()
        self.dragger = Dragger()
    
    #Show Methods
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) #light green
                else:
                    color = (119, 154, 88) # dark green
                
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                
                pygame.draw.rect(surface, color, rect)
    
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)
                        
    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            
            # Loop all valid moves
            for move in piece.moves:
                # color
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                # rect
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)
                

    def show_last_move(self, surface):
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
            
            for pos in [initial, final]:
                # color
                color = (244, 247, 116) if (pos.row + pos.col) % 2 == 0 else (172, 195, 51)
                # rect
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)
    
        
    
    # other methods 
    
    def next_turn(self):
        if self.next_player == 'black':
            self.next_player = 'white'
        else:
            self.next_player = 'black'