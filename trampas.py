from typing import Any
import pygame
from constantes import *
from auxiliar import Auxiliar
from enemigo import *

class Trampa(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, scale=1):
        super().__init__()
        self.scale = scale
        self.image = pygame.image.load(image_path)
        #self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale), int(self.image.get_height() * self.scale)))
        self.image = pygame.transform.rotozoom(self.image, 0, self.scale )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)