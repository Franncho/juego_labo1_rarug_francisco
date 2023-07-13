import pygame
from constantes import *
from auxiliar import Auxiliar

class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion, player, p_scale=1, numero_objeto=None):
        super().__init__()
        self.numero_objeto=numero_objeto
        self.player = player
        if self.numero_objeto==1:
            self.disparo_d = Auxiliar.getSurfaceFromSeparateFiles("images/Object/bullet_player/{0}.png", 1, 5, flip=False, scale=p_scale)
            self.disparo_i = Auxiliar.getSurfaceFromSeparateFiles("images/Object/bullet_player/{0}.png", 1, 5, flip=True, scale=p_scale)
        if self.numero_objeto==2:
            self.disparo_d = Auxiliar.getSurfaceFromSeparateFiles("images/Object/bullet_enemy/bullet_enemy_3/{0}.png", 0, 4, flip=False, scale=p_scale)
            self.disparo_i = Auxiliar.getSurfaceFromSeparateFiles("images/Object/bullet_enemy/bullet_enemy_3/{0}.png", 0, 4, flip=True, scale=p_scale)
        if self.numero_objeto==3:
            self.disparo_d = Auxiliar.getSurfaceFromSeparateFiles("images/Object/bullet_enemy/bullet_enemy_2/{0}.png", 0, 4, flip=False, scale=p_scale)
            self.disparo_i = Auxiliar.getSurfaceFromSeparateFiles("images/Object/bullet_enemy/bullet_enemy_2/{0}.png", 0, 4, flip=True, scale=p_scale)
        if self.numero_objeto==4:
            self.disparo_d = Auxiliar.getSurfaceFromSeparateFiles("images/Object/bullet_enemy/bullet_boss/{0}.png", 0, 4, flip=False, scale=p_scale)
            self.disparo_i = Auxiliar.getSurfaceFromSeparateFiles("images/Object/bullet_enemy/bullet_boss/{0}.png", 0, 4, flip=True, scale=p_scale)

        self.direccion = direccion
        self.velocidad = 5  # Velocidad de movimiento del objeto
        self.frame = 0
        if direccion == DIRECTION_R:
            self.animaciones = self.disparo_d
        elif direccion == DIRECTION_L:
            self.animaciones = self.disparo_i
            self.velocidad *= -1  # Invierte la velocidad para moverse hacia la izquierda
        else:
            self.animaciones = None
        self.image = self.animaciones[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += self.velocidad
        self.frame += 1
        if self.frame >= len(self.animaciones):
            self.frame = 0
        self.image = self.animaciones[self.frame]
        # Si el objeto sale de la ventana, se elimina
        if self.rect.right < 0 or self.rect.left > ANCHO_VENTANA:
            self.player.attack_launched = False
            self.kill()






