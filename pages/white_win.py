import pygame
import sys

from pages import second_page
from widgets import image
from widgets import button
from widgets import size
from widgets import text
from data import colors

def page(screen, users):
    x, y = screen.get_size()
    
    winner_name = users[1].upper()
    winner_text = text.Text(
        screen, 
        f'{winner_name} WINS!', 
        x // 2, 250, 80, 
        fg_color=colors.gray_dark
    )
    
    quit_button_size = size.Size(480, 500, 130, 50)
    quit_button = button.Button(screen, quit_button_size, 'QUIT')
    
    rematch_button_size = size.Size(720, 500, 130, 50)
    rematch_button = button.Button(screen, rematch_button_size, 'REMATCH')
    
    while True:
        screen.fill(colors.white)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if quit_button.onTap(event):
                sys.exit()
            if rematch_button.onTap(event):
                second_page.page(screen, users)
            
            quit_button.onHover(event)
            rematch_button.onHover(event)
            
        winner_text.draw()
        quit_button.draw()
        rematch_button.draw()
        
        pygame.display.update()
