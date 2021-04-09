from datetime import datetime
import pygame

import size


class TextField:
    def __init__(self, screen, size, controller, font="freesansbold.ttf", enable=True):
        self.screen = screen
        self.size = size
        self.controller = controller
        self.font = font
        self._rect = pygame.Rect(self.size.x, self.size.y, self.size.width, self.size.height)
        self._enable = enable
        self.__type = enable
        self.__color = (70, 70, 225) if enable else (170, 170, 170)

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
        textFont = pygame.font.Font(self.font, self.size.height - 14)
        textSurface = textFont.render(self.controller.text, True, (0, 0, 0))
        textRect = textSurface.get_rect()
        textRect.center = self.size.center
        self.screen.blit(textSurface, textRect)
        if textRect.width + 50 > self.rect.width:
            self.canType = False
            self.color = (255, 30, 30)
        elif textRect.width + 50 < self.rect.width:
            self.canType = True
            self.color = (70, 70, 225)


    def draw_button(self):
        buttonSize = size.Size(self.size.right + 20, self.size.top + 5, 60, self.size.height - 10)
        buttonRect = pygame.Rect(buttonSize.x, buttonSize.y, buttonSize.width, buttonSize.height)
        textFont = pygame.font.Font(self.font, self.size.height - 36)
        textSurface = textFont.render("Done!", True, (255, 255, 255))
        textRect = textSurface.get_rect()
        textRect.center = buttonSize.center
        pygame.draw.rect(self.screen, (70, 70, 225), buttonRect)
        self.screen.blit(textSurface, textRect)

    def typing(self, event):
        if event.type == pygame.KEYDOWN and self.enable:
            if event.key == pygame.K_BACKSPACE:
                self.controller.text = self.controller.text[:-1]
            elif self.canType:
                try:
                    self.controller.text += chr(event.key)
                except:
                    pass

    def onTap(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos[0], event.pos[1]):
                self.color = (70, 70, 255)
                self.enable = True
            if not self.rect.collidepoint(event.pos[0], event.pos[1]):
                self.color = (170, 170, 170)
                self.enable = False

    def onDone(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                return True

    @property
    def time(self):
        return self._time

    @property
    def color(self):
        return self.__color

    @property
    def enable(self):
        return self._enable

    @property
    def rect(self):
        return self._rect

    @property
    def canType(self):
        return self.__type

    @time.setter
    def time(self, value):
        self._time = value

    @color.setter
    def color(self, value):
        self.__color = value

    @enable.setter
    def enable(self, value):
        self._enable = value

    @rect.setter
    def rect(self, value):
        self._rect = value

    @canType.setter
    def canType(self, value):
        self.__type = value


def shouldRepaintPointer(time):
    if datetime.now().second - time >= 2:
        return True
    return False
