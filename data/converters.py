def pos_to_list(pos):
    return [ord(pos[0]) - 97, int(pos[1]) - 1]
    
def list_to_pos(lst):
    return f'{chr(lst[0]+97)}{lst[1]+1}'

def pixel_to_list(pixel, sqr_size, table_size):
    return [
        ((pixel[0] - table_size.left) // sqr_size), 
         7 - ((pixel[1] - table_size.top) // sqr_size)
    ]

def pixel_to_pos(pixel, sqr_size, table_size):
    return list_to_pos(pixel_to_list(pixel, sqr_size, table_size))