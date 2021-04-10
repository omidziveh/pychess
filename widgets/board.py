import pygame

from data import colors


class Board:
    def __init__(self, screen, table_size, side, sqr_size, padding=100, theme=(colors.gray_dark, colors.gray_light), width=2):
        self.screen = screen  # pygame.display
        self.size = table_size  # Size
        self.side = side  # "colors.white" / "colors.black"
        self.sqr_size = sqr_size # int
        self.theme = theme  # (color dark, color light)
        self.padding = padding  # Integer
        self.width = width  # Integer
        self._rect = pygame.Rect(self.size.x, self.size.y, self.size.width, self.size.height)
        self._pieces = {}
    
    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.theme[0],
            self.rect
        )

        for i in range(self.size.left, self.size.right, self.sqr_size * 2):
            for j in range(self.size.top, self.size.bottom, self.sqr_size * 2):
                pygame.draw.rect(
                    self.screen,
                    self.theme[1],
                    (i, j, self.sqr_size, self.sqr_size)
                )

        for i in range(self.size.left + self.sqr_size, self.size.right, self.sqr_size * 2):
            for j in range(self.size.top + self.sqr_size, self.size.bottom, self.sqr_size * 2):
                pygame.draw.rect(
                    self.screen,
                    self.theme[1],
                    (i, j, self.sqr_size, self.sqr_size)
                )

    def coord(self, pos):
        rect = ((pos[0] - self.size.left) // self.sqr_size, 7 - (pos[1] - self.size.top) // self.sqr_size)
        return f'{rect[1]+1}{chr(97+rect[0])}'

    # def generate_fen(self, string):
    #     string = string.split()[0]
    #     piece_list = string.split('/')
    #     new_string = []
    #     print(string)
    #     for i in range(len(piece_list)):
    #         new_string.append(split_numbers(piece_list[i]))
    #     return new_string

    def draw_piece(self, point):
        print(8-int(point[0]))
        print(ord(point[1]) - 97)
        piece_rect = pygame.Rect(
            (ord(point[1]) - 97) * self.sqr_size + self.size.left,
            (8-int(point[0])) * self.sqr_size + self.size.top,
            self.sqr_size,
            self.sqr_size
        )
        pygame.draw.rect(
            self.screen,
            colors.green,
            piece_rect
        )


    @property
    def rect(self):
        return self._rect

    @property
    def pieces(self):
        return self._pieces

    @rect.setter
    def rect(self, value):
        self._rect = value

    @pieces.setter
    def pieces(self, value):
        self._pieces = value


def convert_fen_piece_to_uri(string):
    piece_name = ['k', 'q', 'b', 'n', 'r', 'p', 'K', 'Q', 'B', 'N', 'R', 'P']
    complete_name = ['Wk', 'Wq', 'Wb', 'Wn', 'Wr', 'Wp', 'Bk', 'Bq', 'Bb', 'Bn', 'Br', 'Bp']
    if string in piece_name:
        pass
