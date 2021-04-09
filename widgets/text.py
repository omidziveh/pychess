import pygame

from data import colors


pygame.init()


class Text:
    def __init__(self, screen, string, center_x, center_y, height,
                 font="freesansbold.ttf", fg_color=colors.white, bg_color=None):

        self.screen = screen
        self.fg_color = fg_color
        self.bg_color = bg_color

        self.font = pygame.font.Font(font, height)
        self.text = self.font.render(string, True, fg_color, bg_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (center_x, center_y)

    def draw(self):
        self.screen.blit(self.text, self.text_rect)
