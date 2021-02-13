import pygame
import sys

import board
import colors

pygame.init()

screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)

board = board.Board(screen, (10, 20), 30)

while True:
    screen.fill(colors.white)
    
    board.draw()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()