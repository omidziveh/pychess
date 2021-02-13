import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            quit()