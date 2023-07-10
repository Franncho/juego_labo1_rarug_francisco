import pygame
from auxiliar import *
from constantes import *

class PlataformaMovil(pygame.sprite.Sprite):
    def __init__(self, x, y, desplazamiento, width, height, velocidad, movimiento=0, type=1):
        super().__init__()
        self.width = width
        self.height = height
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("images/tileset/forest/Tiles/{0}.png", 1, 14, flip=False, w=width, h=height)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.desplazamiento = desplazamiento
        self.direccion = 1  # Dirección inicial (1: derecha, -1: izquierda)
        self.velocidad = velocidad
        self.movimiento = movimiento

    def update(self, start_x, end_x, start_y, end_y):
        if self.movimiento == 0:  # Movimiento en el eje X
            self.rect.x += self.desplazamiento * self.direccion * self.velocidad
            if self.rect.x <= start_x or self.rect.x >= end_x - self.rect.width:
                self.direccion *= -1
            self.collision_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 10)

        elif self.movimiento == 1:  # Movimiento en el eje Y
            self.rect.y += self.desplazamiento * self.direccion * self.velocidad
            if self.rect.y <= start_y or self.rect.y >= end_y - self.rect.height:
                self.direccion *= -1
            self.collision_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 10)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if DEBUG:
            pygame.draw.rect(screen, C_BLUE, self.collision_rect)

