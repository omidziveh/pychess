import pygame

pygame.init()


class Image:
    def __init__(self, screen, path, size):
        self.screen = screen
        self.path = path
        self.size = size
        self.y = self.size.y

        self.image = pygame.image.load(path)

        self.image = pygame.transform.scale(self.image, (size.width, size.height))

    def draw(self):
        self.screen.blit(self.image, (self.size.x, self.size.y))
    
    def onTap(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.size.rect.collidepoint(event.pos):
                self.size.y += 3
        if event.type == pygame.MOUSEBUTTONUP:
            self.size.y = self.y
            if self.size.rect.collidepoint(event.pos):
                return True

