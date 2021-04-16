import pygame

from widgets import image


class Piece:
    def __init__(self, screen, path, size):
        self.screen = screen
        self.path = path
        self.size = size

        self.image = image.Image(screen, path, size)
    
    def draw(self):
        self.image.draw()
    
    def onTap(self, event):
        return self.image.onTap(event)
    