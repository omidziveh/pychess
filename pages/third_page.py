import pygame
import sys

from data import colors
from widgets import texteditingcontroller
from widgets import textfield
from widgets import button
from widgets import image
from widgets import text
from widgets import size
from pages import second_page
from pages import forth_page
from pages import loading

pygame.init()


def page(screen, users={1: 'player1', 2: 'player2'}):

    # ----- TextField -----
    player2_name_text = text.Text(
        screen, 'Player 2 name:', 460, 250, 18, fg_color=colors.gray_dark)
    player2_name_texteditingcontroller = texteditingcontroller.TextEditingController()
    player2_name_size = size.Size(710, 250, 250, 50)
    player2_name_textfield = textfield.TextField(
        screen, player2_name_size, player2_name_texteditingcontroller, default_text=users[2])

    # ----- "next" button -----
    next_button_size = size.Size(600, 500, 100, 50)
    next_button = button.Button(screen, next_button_size, 'Start!', border=13)

    # ----- back button -----
    back_button_size = size.Size(50, 50, width=70, height=70)
    back_button = image.Image(
        screen, 'assets/icons/back.png', back_button_size)

    # ----- Main loop -----
    while True:
        screen.fill(colors.white)

        # ---- Events ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if next_button.onTap(event): # NEXT
                player2_name = player2_name_texteditingcontroller.text
                users[2] = player2_name
                loading.page(screen)
                forth_page.page(screen, users)

            player2_name_textfield.typing(event)

            if back_button.onTap(event): # BACK
                users[2] = player2_name_texteditingcontroller.text
                second_page.page(screen, users)

            next_button.onHover(event) # NEXT(hover)

        # ---- TextField ----
        player2_name_text.draw()
        player2_name_textfield.draw()
        
        # ---- buttons ----
        next_button.draw()
        back_button.draw()

        # ---- Updates ----
        pygame.display.update()
        pygame.time.Clock().tick(60)
