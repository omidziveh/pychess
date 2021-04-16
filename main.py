import pygame

from pages import first_page

pygame.init()

screen_size = (900, 600)
screen = pygame.display.set_mode(screen_size)

first_page.page(screen)
