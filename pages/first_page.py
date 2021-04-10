import pygame
from pygame.locals import *
import sys
import os

from pages import second_page
from data import colors
from widgets import button
from widgets import size
from widgets import image


_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                print(canonicalized_path)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def page(screen):

    start_button_size = size.Size(450, 500, width=100, height=50)
    start_button = button.Button(screen, start_button_size, "play", border=13)

    logo_size = size.Size(450, 250, 550, 550)
    logo = image.Image(screen, 'assets\logo.png', logo_size)
    # image = pygame.image.load(os.path.join('pages', 'logo.png'))
    # print(os.path.join('pages', 'logo.png'))
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
        logo.draw()
        # screen.blit(image, (0, 0))
        # screen.blit(image, (0, 0))

        pygame.display.update()
