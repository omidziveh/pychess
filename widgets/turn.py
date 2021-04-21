import pygame

from widgets import image
from widgets import text
from widgets import piece
from widgets import size
from data import colors

pygame.init()


class Turn:
    def __init__(self, screen, turn_size, turn):
        self.screen = screen
        self.size = turn_size
        self._turn = turn
        
        self.path = 'assets/pieces/Wp.png' if turn == 'white' else 'assets/pieces/BP.png'
        
        self.turn_text = text.Text(
            screen, 
            turn+' turn', 
            turn_size.center[0], 
            turn_size.center[1], 
            turn_size.height,
            fg_color=colors.blue_dark
        )
        
        self.turn_piece_size = size.Size(self.size.right + 20, self.size.center[1], 40, 40)
        self.turn_piece = image.Image(
            screen, 
            self.path, 
            self.turn_piece_size, 
            default_tap=False
        )
    
    def draw(self):
        self.turn_text.draw()
        self.turn_piece.draw()
        
    def switch_turn(self):
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'
        print(self.turn)
        
    def switch_path(self):
        if self.path == 'assets/pieces/Wp.png':
            self.path = 'assets/pieces/BP.png'
        else:
            self.path = 'assets/pieces/Wp.png'
            
    def switch_text(self):
        if self.turn == 'white':
            self.turn_text.fg_color = colors.m

    @property
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self, value):
        self._turn = value
        self.turn_text = text.Text(
            self.screen, 
            self._turn+' turn', 
            self.size.center[0], 
            self.size.center[1], 
            self.size.height,
            fg_color=colors.blue_dark
        )
        self.switch_path()
        self.turn_piece = image.Image(
            self.screen, 
            self.path, 
            self.turn_piece_size, 
            default_tap=False
        )