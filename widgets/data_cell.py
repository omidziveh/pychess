import pygame

pygame.init()


class DataCell:
    def __init__(self, screen, string, data_table, row, cell_image=None, cell_image_size=None):
        self.screen = screen
        self.string = string
        self.data_table = data_table
        self.row = row
        self.image = cell_image
        self.image_size = cell_image_size
