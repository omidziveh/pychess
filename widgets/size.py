import pygame


class Size:
    def __init__(self, center_x, center_y, width=None, height=None, radius=None):
        self.x = center_x - width // 2
        self.y = center_y - height // 2
        self.center = [center_x, center_y]

        self.width = width
        self.height = height
        self.radius = radius

        self.left = self.x
        self.right = self.x + width
        self.top = self.y
        self.bottom = self.y + height

        self._rect = pygame.Rect(self.x, self.y, width, height)
        self.circle = (center_x, center_y, radius)

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value
        self.center = value.center
