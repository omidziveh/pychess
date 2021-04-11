from typing import MutableMapping
import pygame
import sys

from data import colors
from widgets import board
from widgets import size
from widgets import menu
from widgets import datas

pygame.init()

def page(screen, users):
    table_size = size.Size(230, 300, 360, 360)
    table = board.Board(screen, table_size, 'w', 45)
    data_table_size = size.Size(700, 300, width=300, height=400)
    data_table = datas.Datas(screen, (100, 100), data_table_size)
    my_menu = menu.Menu(screen, [])
    
    while True:
        screen.fill(colors.white)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if not my_menu.enabled:
                pass
            if data_table.menu_button_tapped(event):
                my_menu.enabled = True
        
        table.draw()
        data_table.draw()
        
        if my_menu.enabled:
            my_menu.draw()
        
        pygame.display.update()
