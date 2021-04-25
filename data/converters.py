def pos_to_list(pos):
    try:
        return [ord(pos[0]) - 97, int(pos[1]) - 1]
    except:
        return pos
    
def list_to_pos(lst):
    return f'{chr(lst[0]+97)}{lst[1]+1}'

def pixel_to_list(pixel, sqr_size, table_size):
    return [
        ((pixel[0] - table_size.left) // sqr_size), 
         7 - ((pixel[1] - table_size.top) // sqr_size)
    ]

def pixel_to_pos(pixel, sqr_size, table_size):
    return list_to_pos(pixel_to_list(pixel, sqr_size, table_size))

def list_to_pixel(lst, sqr_size, table_size):
    return [
        (lst[0]) * sqr_size + table_size.left,
        table_size.bottom - (lst[1]+1) * sqr_size
    ]

def number_to_pixel(number, sqr_size, table_size):
    i, j = number // 8, number % 8
    return [
        table_size.left + i * sqr_size, 
        table_size.top + j * sqr_size
    ]
