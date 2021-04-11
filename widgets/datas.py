import pygame

from data import colors
from widgets import size

pygame.init()

class Datas:
    def __init__(self, screen, cell_size, table_size, 
                 colors={'light': colors.gray_light, 'dark': colors.gray_dark}):
        self.screen = screen
        self.cell_size = cell_size
        self.table_size = table_size
        self.colors = colors
        self.inside_table_size = size.Size(
            table_size.center[0], 
            table_size.center[1] + 15, 
            table_size.width - 30, 
            table_size.height - 60
        )

    def draw(self):
        pygame.draw.rect(
            self.screen, 
            self.colors['dark'], 
            self.table_size.rect, 
            border_radius=13
        )
        pygame.draw.rect(
            self.screen, 
            self.colors['light'], 
            self.inside_table_size.rect, 
            border_radius=13
        )
