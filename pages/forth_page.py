import pygame
import chess
import sys

from pages import second_page
from pages import black_win
from pages import white_win
from widgets import button
from widgets import board
from widgets import datas
from widgets import size
from widgets import menu
from widgets import text
from data import colors

pygame.init()


def init_check(screen):
    check_size = size.Size(685, 300, 100, 45)
    check_text = text.Text(screen,
                           'CHECK!',
                           685,
                           300,
                           18,
                           fg_color=colors.brown_light)

    return {'size': check_size, 'text': check_text}


def draw_check(screen, init):
    pygame.draw.rect(screen,
                     colors.brown_dark,
                     init['size'].rect,
                     border_radius=4)
    init['text'].draw()


def page(screen, users):

    # ---- init -----
    check = init_check(screen)

    # ---- chess -----
    chess_board = chess.Board()

    # ----- table -----
    table_size = size.Size(300, 300, width=480, height=480)
    table = board.Board(screen, table_size, 'w', 60, chess_board)

    # ----- DataTable -----
    data_table_size = size.Size(1000, 300, width=350, height=500)
    data_table = datas.DataTable(screen, (100, 50), data_table_size)

    # ----- "Quit" button -----
    quit_button_size = size.Size(600, 270, width=250, height=50)
    quit_button = button.Button(screen, quit_button_size, 'QUIT')

    # ----- "Rematch" button -----
    rematch_button_size = size.Size(600, 350, width=250, height=50)
    rematch_button = button.Button(screen, rematch_button_size, 'REMATCH')

    # ----- menu -----
    my_menu = menu.Menu(screen, [quit_button, rematch_button])

    # ----- Main loop -----
    while True:
        screen.fill(colors.white)

        # ---- Events ----
        table.dict_to_list(table.generate_fen())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if my_menu.enabled:  # if the menu is enabled
                if my_menu.onTap_close_button(event):  # close button
                    my_menu.enabled = False

                if my_menu.onTap_button(event, 0):  # QUIT button
                    sys.exit()

                if my_menu.onTap_button(event, 1):  # REAMTCH button
                    second_page.page(screen, users)

            if not my_menu.enabled:  # if the menu is NOT enabled
                if data_table.menu_button_tapped(event):
                    my_menu.enabled = True
                if data_table.undo_button_tapped(event):
                    try:
                        chess_board.pop()
                    except:
                        pass

                if event.type == pygame.MOUSEBUTTONUP:
                    table.tap_move(event.pos)
                    table.onTap_pieces(event.pos)

        # ---- Draw ----
        table.draw()
        data_table.draw()
        table.draw_pieces()
        table.draw_legal_moves()
        if chess_board.is_check():
            draw_check(screen, check)

        if chess_board.is_checkmate():
            if chess_board.turn:
                black_win.page(screen, users)
            else:
                white_win.page(screen, users)

        if my_menu.enabled:  # if menu is enabled
            my_menu.draw(event)

        # ---- Updates ----
        pygame.display.update()
        pygame.time.Clock().tick(60)
