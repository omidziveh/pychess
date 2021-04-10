import pygame
import os

pygame.init()


class Image:
    def __init__(self, screen, path, size):
        self.screen = screen
        self.path = path
        self.size = size

        self.image = pygame.image.load('logo.png')

        pygame.transform.scale(self.image, (size.width, size.height))

    def draw(self):
        self.screen.blit(self.image, (self.size.x, self.size.y))
