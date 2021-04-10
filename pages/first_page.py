import pygame
import sys
import os

from pages import second_page
from data import colors
from widgets import button
from widgets import size
from widgets import image


def page(screen):

    start_button_size = size.Size(450, 500, width=100, height=50)
    start_button = button.Button(screen, start_button_size, "play", border=13)

    # logo_size = size.Size(450, 100, 200, 100)
    # logo = image.Image(screen, 'logo.png', logo_size)
    # image = pygame.image.load('')
    # image = pygame.transform.scale(image, (400, 400))

    while True:
        screen.fill(colors.white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            start_button.onHover(event)
            if start_button.onTap(event):
                second_page.page(screen)

        start_button.draw()
        # logo.draw()
        # screen.blit(image, (0, 0))

        pygame.display.update()
