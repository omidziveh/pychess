import pygame
from pygame.draw import line

import colors

class Board:
    def __init__(self, screen, pos, sqr_size, padding=10, theme="black", width=2):
        self.sqr_size = sqr_size # Integer
        self.screen = screen # pygame.display
        self.pos = pos # (Integer X, Integer Y)
        self.theme = theme # color
        self.padding = padding # Integer
        self.width = width # Integer
    
    def draw(self):
        # draw vertical lines
        for i in range(9):
            pygame.draw.line(
                self.screen,
                colors.black,
                (self.pos[0] + i * self.sqr_size, self.pos[1]),
                (self.pos[0] + i * self.sqr_size, self.pos[1] + 8 * self.sqr_size),
                width=self.width
            )
            
        # draw horizental lines
        for i in range(9):
            pygame.draw.line(
                self.screen, 
                colors.black, 
                (self.pos[0], self.pos[1] + i * self.sqr_size), 
                (self.pos[0] + 8 * self.sqr_size, self.pos[1] + i * self.sqr_size), 
                width=self.width
            )