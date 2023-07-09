import pygame
from auxiliar import *
from constantes import *

class PlataformaMovil(pygame.sprite.Sprite):
    def __init__(self, x, y,desplazamiento, width, height, velocidad):
        super().__init__()
        self.width=width
        self.height=height
        self.image = pygame.image.load("images/tileset/forest/Tiles/4.png")
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.desplazamiento = desplazamiento
        self.direccion = 1  # Dirección inicial (1: derecha, -1: izquierda)
        self.velocidad = velocidad

    def update(self):
        self.rect.x += self.desplazamiento * self.direccion * self.velocidad
        if self.rect.x <= 400 or self.rect.x >= 800 - self.rect.width:  # Limitar el movimiento dentro de la ventana
            self.direccion *= -1
        self.collision_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 10)


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, C_BLUE, self.collision_rect)
