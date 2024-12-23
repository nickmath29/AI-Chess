import pygame
import sys

from const import *
from game import Game
from square import Square


class Main:
    
    def __init__(self):
        #print('init')
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()
        
        
    def mainloop(self):
        
        game = self.game
        screen = self.screen
        board = self.game.board
        dragger = self.game.dragger
        
        while True:
            game.show_bg(screen) #Creating the board
            game.show_pieces(screen)
            
            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)                    
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
                    
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        
                #Motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # We want to update the mouse since 
                        # the blit depends on the mouse
                        game.show_bg(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                
                #click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()              
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
            pygame.display.update()
    
    
main = Main()
main.mainloop()