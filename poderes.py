from typing import Any
import pygame
from constantes import *
from auxiliar import Auxiliar
from enemigo import *

class Poderes(pygame.sprite.Sprite):
    def __init__(self, x, y, path, scale=1):
        super().__init__()
        self.scale = scale
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale), int(self.image.get_height() * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle=0

    def update(self, delta_ms) -> None:
        self.angle+=1
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)