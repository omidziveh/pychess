import chess
import pygame
import os

from data import converters
from data import colors
from widgets import image
from widgets import size
from widgets import piece


class Board:
    def __init__(self, screen, table_size, side, sqr_size, board, 
                 padding=100, theme=(colors.brown_dark, colors.brown_light), width=2):
        self.screen = screen  # pygame.display
        self.size = table_size  # Size
        self.side = side  # "colors.white" / "colors.black"
        self.sqr_size = sqr_size # int
        self.board = board
        self.theme = theme  # (color dark, color light)
        self.padding = padding  # Integer
        self.width = width  # Integer
        self._rect = pygame.Rect(self.size.x, self.size.y, self.size.width, self.size.height)
        self._pieces = {}
        self.piece_list = []
        self._legal_moves_list = []
        self.legal_moves_rect = []
    
    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.theme[1],
            self.rect
        )

        for i in range(self.size.left, self.size.right, self.sqr_size * 2):
            for j in range(self.size.top, self.size.bottom, self.sqr_size * 2):
                pygame.draw.rect(
                    self.screen,
                    self.theme[0],
                    (i, j, self.sqr_size, self.sqr_size)
                )

        for i in range(self.size.left + self.sqr_size, self.size.right, self.sqr_size * 2):
            for j in range(self.size.top + self.sqr_size, self.size.bottom, self.sqr_size * 2):
                pygame.draw.rect(
                    self.screen,
                    self.theme[0],
                    (i, j, self.sqr_size, self.sqr_size)
                )

    def dict_to_list(self, dict):
        self.piece_list.clear()
        keys = dict.keys()
        for key in keys:
            for value in dict[key]:
                self.piece_list.append(
                    piece.Piece(
                        self.screen,
                        'assets/pieces/'+key+'.png',
                        size.Size(
                            value[0] * self.sqr_size + self.size.left + self.sqr_size // 2, 
                            value[1] * self.sqr_size + self.size.top + self.sqr_size // 2, 
                            self.sqr_size, 
                            self.sqr_size
                        ), 
                        self.sqr_size, 
                        self.size
                    )
                )
   
    def generate_fen(self):
        pieces = {
            'Wr': [], 
            'Wn': [], 
            'Wb': [], 
            'Wq': [],
            'Wk': [], 
            'Wp': [], 
            'BR': [], 
            'BN': [], 
            'BB': [], 
            'BQ': [], 
            'BK': [], 
            'BP': []
        }
        fen = self.board.fen().split()[0].split('/')
        for i in range(len(fen)):
            number = 0
            pos = 0
            for j in range(len(fen[i])):
                if fen[i][j].isdigit():
                    number += int(fen[i][j])
                if fen[i][j] in ['r', 'n', 'b', 'q', 'k', 'p']:
                    pieces['W'+fen[i][j]].append([pos+number, i])
                    pos += 1
                if fen[i][j] in ['R', 'N', 'B', 'Q', 'K', 'P']:
                    pieces['B'+fen[i][j]].append([pos+number, i])
                    pos += 1
        return pieces

    def draw_pieces(self):
        for piece in self.piece_list:
            piece.draw()
    
    def onTap_pieces(self, pos):
        for piece in self.piece_list:
            if piece.onTap(pos):
                self.legal_moves_list = piece.legal_moves(list(self.board.legal_moves))
                
    def draw_legal_moves(self):
        for move in self.legal_moves_list:
            move_pos = converters.list_to_pixel(converters.pos_to_list(str(move)[-2:]), self.sqr_size, self.size)
            pygame.draw.circle(
                self.screen, 
                colors.green, 
                (move_pos[0] + self.sqr_size // 2, move_pos[1] + self.sqr_size // 2), 
                self.sqr_size // 2 - 5
            )
    
    def tap_move(self, pos):
        for i in range(len(self.legal_moves_rect)):
            if self.legal_moves_rect[i].collidepoint(pos):
                self.board.push_san(str(self.legal_moves_list[i]))
        


    @property
    def rect(self):
        return self._rect

    @property
    def pieces(self):
        return self._pieces
    
    @property
    def legal_moves_list(self):
        return self._legal_moves_list

    @rect.setter
    def rect(self, value):
        self._rect = value

    @pieces.setter
    def pieces(self, value):
        self._pieces = value
        
    @legal_moves_list.setter
    def legal_moves_list(self, value):
        self._legal_moves_list = value
        self.legal_moves_rect = []
        for move in self._legal_moves_list:
            move_pos = converters.list_to_pixel(converters.pos_to_list(str(move)[-2:]), self.sqr_size, self.size)
            self.legal_moves_rect.append(
                pygame.Rect(
                    move_pos[0], 
                    move_pos[1], 
                    self.sqr_size, 
                    self.sqr_size
                )
            )
