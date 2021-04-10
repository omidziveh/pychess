import pygame

from data import colors


class TextField:
    def __init__(self, screen, rect_size, controller, font=""):
        self.screen = screen
        self.size = rect_size
        self.controller = controller
        self.font = font
        self._rect = pygame.Rect(self.size.x, self.size.y, self.size.width, self.size.height)
        self.__color = colors.gray_dark

    def draw(self):
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            self.rect
        )
        pygame.draw.rect(
            self.screen,
            self.color,
            self.rect,
            5,
            border_radius=10,
        )
        #  draw the text
        textFont = pygame.font.SysFont(self.font, self.size.height - 14)
        textSurface = textFont.render(self.controller.text, True, (0, 0, 0))
        textRect = textSurface.get_rect()
        textRect.center = self.size.center
        self.screen.blit(textSurface, textRect)
        if textRect.width + 50 > self.rect.width:
            self.canType = False
            self.color = (255, 30, 30)
        elif textRect.width + 50 < self.rect.width:
            self.canType = True
            self.color = colors.gray_dark

    def typing(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.controller.text = self.controller.text[:-1]
            elif self.canType:
                try:
                    self.controller.text += chr(event.key)
                except:
                    pass

    @property
    def color(self):
        return self.__color

    @property
    def rect(self):
        return self._rect

    @color.setter
    def color(self, value):
        self.__color = value

    @rect.setter
    def rect(self, value):
        self._rect = value
