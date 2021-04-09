import pygame
import sys

from data import colors
from widgets import button
from widgets import size


def page():
    screen_size = (900, 600)
    screen = pygame.display.set_mode(screen_size)
    start_button_size = size.Size(450, 450, width=100, height=50)
    start_button = button.Button(screen, start_button_size, "play", border=13)

    while True:
        screen.fill(colors.white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            start_button.onHover(event)
            start_button.onTap(event)

        start_button.draw()

        pygame.display.update()
