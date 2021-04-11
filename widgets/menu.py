import pygame

from widgets import size

pygame.init()


class Menu:
    def __init__(self, screen, buttons, name="menu", enabled=False, width=300, height=300):
        self.screen = screen
        self.buttons = buttons
        self.name = name
        self.enabled = enabled
        self.display_size = {
            'width': pygame.display.get_surface().get_width(), 
            'height': pygame.display.get_surface().get_height()
        }
        self.size = size.Size(
            pygame.display.get_surface().get_width() // 2, 
            pygame.display.get_surface().get_height() // 2, 
            width=width, 
            height=height
        )
        
    def draw(self):
        self.disconnect_display()
        
    
    def disconnect_display(self):
        rect_surface = pygame.Surface(
            (self.display_size['width'], self.display_size['height'])
        ).convert_alpha()
        rect_surface.fill((0, 0, 0, 130))
        self.screen.blit(
            rect_surface, 
            rect_surface.get_rect()
        )
        self.enabled = True
