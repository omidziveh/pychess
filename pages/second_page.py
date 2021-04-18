import pygame
import sys

from data import colors
from widgets import text
from widgets import textfield
from widgets import texteditingcontroller
from widgets import size
from widgets import button
from widgets import image
from pages import third_page
from pages import first_page

pygame.init()


def page(screen):

    player1_name_text = text.Text(screen, 'Player 1 name:', 400, 250, 40, fg_color=colors.gray_dark)
    player1_name_texteditingcontroller = texteditingcontroller.TextEditingController()
    player1_name_size = size.Size(700, 250, 350, 60)
    player1_name_textfield = textfield.TextField(screen, player1_name_size, player1_name_texteditingcontroller)
    next_button_size = size.Size(600, 500, 100, 50)
    next_button = button.Button(screen, next_button_size, 'next', border=13)
    back_button_size = size.Size(50, 50, width=70, height=70)
    back_button = image.Image(screen, 'assets/back.png', back_button_size)

    while True:
        screen.fill(colors.white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # player1_name_textfield.onTap(event)
            player1_name_textfield.typing(event)

            if next_button.onTap(event):
                player1_name = player1_name_texteditingcontroller.text
                third_page.page(screen, {1: player1_name})

            if back_button.onTap(event):
                first_page.page(screen)
            
            next_button.onHover(event)

        player1_name_text.draw()
        player1_name_textfield.draw()
        next_button.draw()
        back_button.draw()

        pygame.display.update()
        pygame.time.Clock().tick(60)
