import pygame
import time

from widgets import image
from widgets import size

pygame.init()

def page(screen):
    loading_image_size = size.Size(600, 300, 1210, 605)
    loading_image = image.Image(screen, 'assets/icons/loading.png', loading_image_size)
    
    loading_image.draw()
    pygame.display.update()
    
    time.sleep(1)
    return
