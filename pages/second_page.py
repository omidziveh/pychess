import pygame
import json
import sys

from data import colors
from widgets import texteditingcontroller
from widgets import textfield
from widgets import button
from widgets import image
from widgets import text
from widgets import size

from pages import first_page
from pages import third_page

pygame.init()


def page(screen, users={1: 'player1', 2:'player2'}):

    # ----- TextField -----
    player1_name_text = text.Text(
        screen, 'Player 1 name:', 400, 250, 40, fg_color=colors.gray_dark)
    player1_name_texteditingcontroller = texteditingcontroller.TextEditingController()
    player1_name_size = size.Size(700, 250, 350, 60)
    player1_name_textfield = textfield.TextField(screen, player1_name_size,
                                                 player1_name_texteditingcontroller,
                                                 default_text=users[1]
                                                 )
    
    # ----- "next" button -----
    next_button_size = size.Size(600, 500, 100, 50)
    next_button = button.Button(screen, next_button_size, 'next', border=13)
    
    # ----- back button -----
    back_button_size = size.Size(50, 50, width=70, height=70)
    back_button = image.Image(screen, 'assets/icons/back.png', back_button_size)

    # ----- Main loop -----
    while True:
        screen.fill(colors.white)

        # ---- Events ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # EXIT
                sys.exit()

            player1_name_textfield.typing(event)

            if next_button.onTap(event): # NEXT
                player1_name = player1_name_texteditingcontroller.text
                users[1] = player1_name
                third_page.page(screen, users) # NAVIGATOR

            if back_button.onTap(event): # BACK
                first_page.page(screen)

            next_button.onHover(event) # NEXT(hover)

        # ---- TextField ----
        player1_name_text.draw()
        player1_name_textfield.draw()
        
        # ---- buttons ----
        next_button.draw()
        back_button.draw()

        # ---- Updates ----
        pygame.display.update()
        pygame.time.Clock().tick(60)
