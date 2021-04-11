import pygame
import sys

from data import colors
from widgets import texteditingcontroller
from widgets import textfield
from widgets import button
from widgets import image
from widgets import text
from widgets import size
from pages import forth_page
from pages import second_page

pygame.init()


def page(screen, users):
    player2_name_text = text.Text(screen, 'Player 2 name:', 300, 250, 30, fg_color=colors.gray_dark)
    player2_name_texteditingcontroller = texteditingcontroller.TextEditingController()
    player2_name_size = size.Size(550, 250, 300, 50)
    player2_name_textfield = textfield.TextField(screen, player2_name_size, player2_name_texteditingcontroller)
    next_button_size = size.Size(450, 500, 100, 50)
    next_button = button.Button(screen, next_button_size, 'Start!', border=13)
    back_button_size = size.Size(50, 50, width=70, height=70)
    back_button = image.Image(screen, 'assets/back.png', back_button_size)
    
    while True:
        screen.fill(colors.white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            player2_name_textfield.typing(event)
            if next_button.onTap(event):
                player2_name = player2_name_texteditingcontroller.text
                users[2] = player2_name
                forth_page.page(screen, users)
            if back_button.onTap(event):
                second_page.page(screen)
            
            next_button.onHover(event)

        player2_name_text.draw()
        player2_name_textfield.draw()
        next_button.draw()
        back_button.draw()

        pygame.display.update()
        pygame.time.Clock().tick(60)
