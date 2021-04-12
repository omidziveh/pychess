from typing import MutableMapping
import pygame
import sys

from data import colors
from widgets import board
from widgets import size
from widgets import menu
from widgets import datas
from widgets import button
from pages import second_page

pygame.init()

def page(screen, users):
    
    table_size = size.Size(230, 300, 360, 360)
    table = board.Board(screen, table_size, 'w', 45)
    data_table_size = size.Size(700, 300, width=300, height=400)
    data_table = datas.DataTable(screen, (100, 100), data_table_size, 2)
    quit_button_size = size.Size(450, 270, width=250, height=50)
    quit_button = button.Button(screen, quit_button_size, 'QUIT')
    rematch_button_size = size.Size(450, 350, width=250, height=50)
    rematch_button = button.Button(screen, rematch_button_size, 'REMATCH')
    my_menu = menu.Menu(screen, [quit_button, rematch_button])
    
    while True:
        screen.fill(colors.white)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if not my_menu.enabled:
                if data_table.menu_button_tapped(event):
                    my_menu.enabled = True
            if my_menu.enabled:
                
                if my_menu.onTap_close_button(event): # close button
                    my_menu.enabled = False
                
                if my_menu.onTap_button(event, 0): # QUIT button
                    sys.exit()
                
                if my_menu.onTap_button(event, 1): # REAMTCH button
                    second_page.page(screen)
        
        table.draw()
        data_table.draw()
        
        if my_menu.enabled:
            my_menu.draw(event)
        
        pygame.display.update()
        pygame.time.Clock().tick(60)
