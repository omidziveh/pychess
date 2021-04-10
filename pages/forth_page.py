import pygame
import sys

from data import colors
from widgets import board
from widgets import size

pygame.init()

def page(screen, users):
    
    table_size = size.Size(230, 300, 360, 360)
    table = board.Board(screen, table_size, 'w', 45)
    
    while True:
        screen.fill(colors.white)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        table.draw()
        
        pygame.display.update()
