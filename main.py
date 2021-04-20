import pygame

from pages import first_page

pygame.init()

screen_size = (1200, 600)
screen = pygame.display.set_mode(screen_size)
first_page.page(screen)
