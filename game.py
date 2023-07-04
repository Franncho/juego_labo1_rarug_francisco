import pygame
from constantes import *
from auxiliar import Auxiliar

class game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.game_over=False