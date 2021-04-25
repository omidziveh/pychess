import pygame
import chess
import time

from data import converters
from data import colors
from widgets import size
from widgets import piece
from pygame import mixer

mixer.init()

class Board:
    def __init__(self, screen, table_size, side, sqr_size, board=chess.Board(), 
                 padding=100, theme=(colors.brown_light, colors.brown_dark), width=2):
        self.screen = screen  # pygame.display
        self.size = table_size  # Size
        self.side = side  # "colors.white" / "colors.black"
        self.sqr_size = sqr_size # int
        self.board = board
        self.theme = theme  # (color dark, color light)
        self.padding = padding  # Integer
        self.width = width  # Integer
        self._rect = pygame.Rect(self.size.x - 22, self.size.y - 22, self.size.width - 40, self.size.height - 40)
        
        self._pieces = {}
        self.piece_list = []
        self._legal_moves_list = []
        self.legal_moves_rect = []
        
    
    def draw(self):
        # pygame.draw.rect(
        #     self.screen,
        #     colors.blue_dark,
        #     self.rect,
        #     width=10,
        #     border_radius=4
        # )
        
        for i in range(self.size.left + self.sqr_size, self.size.right, self.sqr_size * 2):
            for j in range(self.size.top, self.size.bottom, self.sqr_size * 2):
                pygame.draw.rect(
                    self.screen,
                    self.theme[1],
                    (i, j, self.sqr_size - 3, self.sqr_size - 3), 
                    border_radius=4
                )

        for i in range(self.size.left, self.size.right, self.sqr_size * 2):
            for j in range(self.size.top + self.sqr_size, self.size.bottom, self.sqr_size * 2):
                pygame.draw.rect(
                    self.screen,
                    self.theme[1],
                    (i, j, self.sqr_size - 3, self.sqr_size - 3), 
                    border_radius=4
                )
        
        for i in range(self.size.left, self.size.right, self.sqr_size * 2):
            for j in range(self.size.top, self.size.bottom, self.sqr_size * 2):
                pygame.draw.rect(
                    self.screen,
                    self.theme[0],
                    (i, j, self.sqr_size - 3, self.sqr_size - 3), 
                    border_radius=4
                )

        for i in range(self.size.left + self.sqr_size, self.size.right, self.sqr_size * 2):
            for j in range(self.size.top + self.sqr_size, self.size.bottom, self.sqr_size * 2):
                pygame.draw.rect(
                    self.screen,
                    self.theme[0],
                    (i, j, self.sqr_size - 3, self.sqr_size - 3), 
                    border_radius=4
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
                            value[0] * self.sqr_size + self.size.left + self.sqr_size // 2 - 2, 
                            value[1] * self.sqr_size + self.size.top + self.sqr_size // 2 - 2, 
                            self.sqr_size - 4, 
                            self.sqr_size - 4
                        ), 
                        self.sqr_size, 
                        self.size
                    )
                )
   
    def generate_fen(self):
        pieces = {
            'WR': [], 
            'WN': [], 
            'WB': [], 
            'WQ': [],
            'WK': [], 
            'WP': [], 
            'Br': [], 
            'Bn': [], 
            'Bb': [], 
            'Bq': [], 
            'Bk': [], 
            'Bp': []
        }
        fen = self.board.fen().split()[0].split('/')
        for i in range(len(fen)):
            number = 0
            pos = 0
            for j in range(len(fen[i])):
                if fen[i][j].isdigit():
                    number += int(fen[i][j])
                if fen[i][j] in ['R', 'N', 'B', 'Q', 'K', 'P']:
                    pieces['W'+fen[i][j]].append([pos+number, i])
                    pos += 1
                if fen[i][j] in ['r', 'n', 'b', 'q', 'k', 'p']:
                    pieces['B'+fen[i][j]].append([pos+number, i])
                    pos += 1
        return pieces

    def draw_pieces(self):
        for piece in self.piece_list:
            piece.draw()
    
    def onTap_pieces(self, pos):
        for piece in self.piece_list:
            if not piece.onTap(pos):
                self.legal_moves_list.clear()
            else:
                self.legal_moves_list = piece.legal_moves(list(self.board.legal_moves))
                return
                
    def draw_legal_moves(self):
        for move in self.legal_moves_list:
            move_pos = converters.list_to_pixel(converters.pos_to_list(str(move)[2:4]), self.sqr_size, self.size)
            pygame.draw.circle(
                self.screen, 
                colors.blue_dark,
                (move_pos[0] + self.sqr_size // 2, move_pos[1] + self.sqr_size // 2), 
                self.sqr_size // 5
            )
    
    def tap_move(self, pos):
        for i in range(len(self.legal_moves_rect)):
            if self.legal_moves_rect[i].collidepoint(pos):
                self.board.push_san(str(self.legal_moves_list[i]))
                self.legal_moves_list = []
                self.legal_moves_rect = []
                
                move = mixer.Sound('assets/sounds/move.mp3')
                mixer.Sound.set_volume(move, 1)
                mixer.Sound.play(move)

                self.legal_moves_list.clear()
                self.legal_moves_rect.clear()
                                
                time.sleep(0.2)
                return 
            
    def draw_cehck(self):
        if self.board.is_check():
            if self.board.turn:
                print()


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
            move_pos = converters.list_to_pixel(converters.pos_to_list(str(move)[2:4]), self.sqr_size, self.size)
            self.legal_moves_rect.append(
                pygame.Rect(
                    move_pos[0], 
                    move_pos[1], 
                    self.sqr_size, 
                    self.sqr_size
                )
            )
