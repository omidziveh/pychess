import pygame
import sys
import chess
from pygame.event import event_name

from data import colors
from widgets import board
from widgets import size
from widgets import menu
from widgets import datas
from widgets import button
from pages import second_page

pygame.init()

def page(screen, users):

    # ----- Variables -----
    chess_board = chess.Board()
    moves = list(chess_board.legal_moves)

    # ----- Widgets -----
    table_size = size.Size(300, 300, width=480, height=480)
    table = board.Board(screen, table_size, 'w', 60, chess_board)
    
    data_table_size = size.Size(1000, 300, width=350, height=500)
    data_table = datas.DataTable(screen, (100, 50), data_table_size)
    
    quit_button_size = size.Size(600, 270, width=250, height=50)
    quit_button = button.Button(screen, quit_button_size, 'QUIT')
    
    rematch_button_size = size.Size(600, 350, width=250, height=50)
    rematch_button = button.Button(screen, rematch_button_size, 'REMATCH')
    
    my_menu = menu.Menu(screen, [quit_button, rematch_button])
    
    # ----- Main loop -----
    
    while True:
        screen.fill(colors.white)
        
        # ---- Event loop ----
        
        table.dict_to_list(table.generate_fen())
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if not my_menu.enabled:
                if data_table.menu_button_tapped(event):
                    my_menu.enabled = True
                if event.type == pygame.MOUSEBUTTONUP:
                    table.onTap_pieces(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        chess_board.push_san('e2e4')
                    if event.key == pygame.K_2:
                        chess_board.push_san('d7d5')
                    if event.key == pygame.K_3:
                        chess_board.push_san('g1f3')
                    if event.key == pygame.K_4:
                        chess_board.push_san('g8f6')
                    if event.key == pygame.K_5:
                        chess_board.push_san('e4d5')
                    if event.key == pygame.K_6:
                        chess_board.push_san('d8d5')
            if my_menu.enabled:
                
                if my_menu.onTap_close_button(event): # close button
                    my_menu.enabled = False
                
                if my_menu.onTap_button(event, 0): # QUIT button
                    sys.exit()
                
                if my_menu.onTap_button(event, 1): # REAMTCH button
                    second_page.page(screen)
        
        # ---- Draw ----
        
        table.draw()
        data_table.draw()
        table.draw_pieces()
        table.draw_legal_moves()
        
        if my_menu.enabled:
            my_menu.draw(event)
        
        # ---- Updates ----
        
        pygame.display.update()
        pygame.time.Clock().tick(60)
