import pygame

pygame.init()


class DataCell:
    def __init__(self, screen, string, data_table, row, column, cell_image=None, cell_image_size=None):
        self.screen = screen
        self.string = string
        self.data_table = data_table
        self.row = row
        self.image = cell_image
        self.image_size = cell_image_size
        self.column = column
        self.cell_rect = self.init_rect()
        
    def init_rect(self):
        cell_rect = pygame.Rect(
            (self.column - 1) * (self.data_table.table_size.width // 2) + 10 + self.data_table.table_size.left,
            (self.row - 1) * (self.data_table.table_size.height // self.data_table.cell_size[1]) +  + self.data_table.table_size.top,
            self.data_table.cell_size[0],
            self.data_table.cell_size[1]
        )
        print(cell_rect)
        return cell_rect
