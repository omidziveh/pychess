import pygame
import sys

from pages import second_page
from data import colors
from widgets import button
from widgets import size
from widgets import image


def page(screen):

    # ----- "Start" button -----
    start_button_size = size.Size(600, 500, width=100, height=50)
    start_button = button.Button(screen, start_button_size, "play", border=13)

    # ----- Logo -----
    logo_size = size.Size(600, 250, 550, 550)
    logo = image.Image(screen, 'assets\icons\logo.png', logo_size)

    # ----- Main loop -----
    while True:
        screen.fill(colors.white)

        # ---- Events ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            start_button.onHover(event)
            if start_button.onTap(event):
                second_page.page(screen)

        start_button.draw() # draw "start" button.
        logo.draw() # draw the app logo image.

        # ---- Updates ----
        pygame.display.update()
        pygame.time.Clock().tick(60)
