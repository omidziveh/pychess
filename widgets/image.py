import pygame
import os

pygame.init()


class Image:
    def __init__(self, screen, path, size):
        self.screen = screen
        self.path = path
        self.size = size

        self.image = pygame.image.load(path)

        self.image = pygame.transform.scale(self.image, (size.width, size.height))

    def draw(self):
        self.screen.blit(self.image, (self.size.x, self.size.y))
    
    def onTap(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.size.rect.collidepoint(event.pos):
                self.size.rect = (self.size.x, 
                                  self.size.y + 3, 
                                  self.width, 
                                  self.height)
        if event.type == pygame.MOUSEBUTTONUP:
            self.size.rect = (self.size.x, 
                              self.size.y, 
                              self.size.width, 
                              self.size.height)
            if self.size.rect.collidepoint(event.pos):
                return True
