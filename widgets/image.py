import pygame
from pygame import mixer

pygame.init()
mixer.init()


class Image:
    def __init__(self, screen, path, size, default_tap=True):
        self.screen = screen
        self.path = path
        self.size = size
        self.default_tap = default_tap
        self.y = self.size.y

        self.image = pygame.image.load(path)

        self.image = pygame.transform.scale(self.image, (size.width, size.height))
        

    def draw(self):
        self.screen.blit(self.image, (self.size.x, self.size.y))
    
    def onTap(self, event):
        if self.default_tap:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.size.rect.collidepoint(event.pos):
                    self.size.y += 3
            if event.type == pygame.MOUSEBUTTONUP:
                self.size.y = self.y
                if self.size.rect.collidepoint(event.pos):
                    click = mixer.Sound('assets/sounds/click.mp3')
                    mixer.Sound.set_volume(click, 1)
                    mixer.Sound.play(click)
                    return True
        if event.type == pygame.MOUSEBUTTONUP:
            if self.size.rect.collidepoint(event.pos):
                return True

