from chess import Move
import pygame

from data import colors
from widgets import text
from pygame import mixer

# pygame.init()
mixer.init()


class Button:
    def __init__(self, screen, button_size, string,
                 foreground_color=colors.gray_light,
                 background_color=colors.gray_dark,
                 border=5):
        self.screen = screen  # pygame.display.set_mode
        self.size = button_size  # size.Size
        self.fg_color = foreground_color  # colors
        self.bg_color = background_color  # colors
        self.border = border  # int
        
        self._text = text.Text(
            screen, string, 
            button_size.center[0], button_size.center[1], 
            18
        )
        
        self.__hovered = False
        self.__string = string

    # draw the button with hover design and text
    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.bg_color,
            self.size.rect,
            border_radius=self.border
        )
        self.text.draw()
        if self.__hovered:
            self.default_hover()

    # check is the button pressed or not
    def onTap(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.size.rect.collidepoint(event.pos):
                self.size.rect = pygame.Rect(self.size.x, self.size.y + 3, self.size.width, self.size.height)
        if event.type == pygame.MOUSEBUTTONUP:
            self.size.rect = pygame.Rect(self.size.x, self.size.y, self.size.width, self.size.height)
            if self.size.rect.collidepoint(event.pos):
                
                move = mixer.Sound('assets/sounds/click.mp3')
                mixer.Sound.set_volume(move, 1)
                mixer.Sound.play(move)
                
                return True

    # check is the button hovered or not
    def onHover(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.size.rect.collidepoint(event.pos):
                self.__hovered = True
                return True
            if not self.size.rect.collidepoint(event.pos):
                self.__hovered = False
                return False

    # default work when the user hover the button
    def default_hover(self):
        hover_color = (self.background_color[0]+50, self.background_color[1]+50, self.background_color[2]+50)
        pygame.draw.rect(
            self.screen,
            hover_color,
            self.size.rect,
            border_radius=self.border,
            width=5
        )

    @property
    def foreground_color(self):
        return self.fg_color

    @property
    def background_color(self):
        return self.bg_color

    @property
    def text(self):
        self._text = text.Text(self.screen,  # update the value of _text
                               self.__string,
                               self.size.center[0],
                               self.size.center[1],
                               self.size.height - 20)
        return self._text

    @foreground_color.setter
    def foreground_color(self, value):
        self.fg_color = value

    @background_color.setter
    def background_color(self, value):
        self.bg_color = value
