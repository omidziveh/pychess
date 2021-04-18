import pygame

from widgets import image
from data import converters


class Piece:
    def __init__(self, screen, path, size, sqr_size, table_size):
        self.screen = screen
        self.path = path
        self.size = size
        self.sqr_size = sqr_size
        self.table_size = table_size

        self.image = image.Image(screen, path, size, default_tap=False)
    
    def draw(self):
        self.image.draw()
    
    def onTap(self, pos):
        return True if self.size.rect.collidepoint(pos) else False
    
    def legal_moves(self, moves_list):
        # print(moves_list)
        legal_moves_list = []
        for move in moves_list:
            pos = converters.pixel_to_pos(
                (self.size.left, self.size.top), 
                self.sqr_size, 
                self.table_size
            )
            # print(pos)
            if str(move)[0] + str(move)[1] == pos:
                legal_moves_list.append(move)
        return legal_moves_list
    
    # def legal_moves(self, moves_list):
    #     for move in moves_list:
    #         # print(move)
    #         print(
    #             converters.pixel_to_pos([self.size.left - self.table_size.left, self.size.top - self.table_size.top], self.size.width, self.table_size),
    #             end=" / "
    #         )
    #         print(str(move)[0] + str(move)[1])
    #         if str(move)[0] + str(move)[1] == converters.pixel_to_pos([self.size.left, self.size.top], self.size.width, self.table_size):
    #             print(move)
