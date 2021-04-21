import pygame

from pages import first_page

pygame.init()

screen_size = (1200, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('pychess')
icon = pygame.image.load('assets/icons/icon.png')
icon = pygame.transform.smoothscale(icon, (96, 96))
pygame.display.set_icon(icon.convert_alpha())
first_page.page(screen)
