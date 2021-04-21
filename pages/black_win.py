import pygame

from data import colors
from widgets import image
from widgets import text
from widgets import size
from widgets import button
from pages import second_page


pygame.init()

def page(screen, users, winner):
    winner_image_size = size.Size()
    winner_image = image.Image(screen, 'assets/icons/'+winner+'_win.png', winner_image_size)
