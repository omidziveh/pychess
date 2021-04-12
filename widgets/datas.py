from widgets.menu import Menu
import pygame

from data import colors
from widgets import size
from widgets import image

pygame.init()

class DataTable:
    def __init__(self, screen, cell_size, table_size, rows,
                 colors={'light': colors.white, 'dark': colors.gray_dark}):
        self.screen = screen
        self.cell_size = cell_size
        self.table_size = table_size
        self.rows = rows
        self.colors = colors
        self.inside_table_size = size.Size(
            table_size.center[0], 
            table_size.center[1] + 15, 
            table_size.width - 30, 
            table_size.height - 60
        )
        self.menu_button = self.init_menu_button()

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
        self.menu_button.draw()
    
    def init_menu_button(self):
        menu_button_size = size.Size(
            self.inside_table_size.right - 20, 
            (self.inside_table_size.top - 20), 
            width=30,
            height=23
        )
        menu_button = image.Image(self.screen, 'assets/menu.png', menu_button_size)
        return menu_button
        
    def menu_button_tapped(self, event):
        if self.menu_button.onTap(event):
            return True
