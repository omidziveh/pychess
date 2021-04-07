import sys
import chess
import pygame

from data import colors
from widgets import board
from widgets import size

code_board = chess.Board()

print(code_board.fen())

screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
#
gui_board = board.Board(screen, size.Size(100, 100, 400, 400), 'w', 50)
# print(gui_board.generate_fen("8/8/8/8/8/8/8 b KQkq - 0 4"))
# print(gui_board.generate_fen("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4"))
# print(gui_board.generate_fen(code_board.fen()))
# print(gui_board.pieces)
# print(code_board)

while True:
    screen.fill(colors.white)

    gui_board.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(gui_board.coord(event.pos))
            gui_board.draw_piece(gui_board.coord(event.pos))
    pygame.display.update()
    pygame.time.Clock().tick(60)
