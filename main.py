import pygame

from pages import start_page

pygame.init()

screen_size = (900, 600)
screen = pygame.display.set_mode(screen_size)

start_page.page(screen)