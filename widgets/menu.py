import pygame

from data import colors
from widgets import size
from widgets import text
from widgets import image

pygame.init()


class Menu:
    def __init__(self, screen, buttons, name="MENU", enabled=False, width=300, height=300):
        self.screen = screen
        self.buttons = buttons
        self.name = name
        self.enabled = enabled
        self.name_text = self.init_name()
        self.close_button = self.init_close_button()
        
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
        
    def draw(self, event):
        if self.enabled:
            self.disconnect_display()
            self.draw_self()
            self.button(event)
            self.name_text.draw()
            self.close_button.draw()
        
    
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
    
    def connect_display(self):
        self.enabled = False

    def draw_self(self):
        pygame.draw.rect(
            self.screen, 
            colors.white, 
            self.size.rect, 
            border_radius = 20
        )
    
    def button(self, event):
        for i in range(len(self.buttons)):
            self.buttons[i].draw()
            self.buttons[i].onHover(event)
            
    def onTap_button(self, event, index):
        return self.buttons[index].onTap(event)
    
    def init_name(self):
        name_text = text.Text(self.screen, self.name, 375, 190, 45, fg_color=colors.gray_dark)
        return name_text
        
    def init_close_button(self):
        close_button_size = size.Size(570, 190, width=40, height=40)
        close_button = image.Image(self.screen, 'assets/close.png', close_button_size)
        return close_button
        
    def draw_close_button(self):
        self.close_button.draw()
        
    def onTap_close_button(self, event):
        return self.close_button.onTap(event)
