import pygame

class TextEditingController:
    def __init__(self):
        self._text = ''
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        self._text = value
