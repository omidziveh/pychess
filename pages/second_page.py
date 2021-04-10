import pygame
import sys

from data import colors
from widgets import text
from widgets import textfield
from widgets import texteditingcontroller
from widgets import size
from widgets import button
from pages import third_page

pygame.init()


def page(screen):

    player1_name_text = text.Text(screen, 'Player 1 name:', 300, 250, 30, fg_color=colors.gray_dark)
    player1_name_texteditingcontroller = texteditingcontroller.TextEditingController()
    player1_name_size = size.Size(550, 250, 300, 50)
    player1_name_textfield = textfield.TextField(screen, player1_name_size, player1_name_texteditingcontroller)
    next_button_size = size.Size(450, 500, 100, 50)
    next_button = button.Button(screen, next_button_size, 'next', border=13)

    while True:
        screen.fill(colors.white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # player1_name_textfield.onTap(event)
            player1_name_textfield.typing(event)
            if next_button.onTap(event):
                third_page.page(screen)
            next_button.onHover(event)

        player1_name_text.draw()
        player1_name_textfield.draw()
        next_button.draw()

        pygame.display.update()
        pygame.time.Clock().tick(60)
