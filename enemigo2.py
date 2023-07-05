import pygame
from constantes import *
from auxiliar import Auxiliar

class Enemy_2(pygame.sprite.Sprite):
    def __init__(self, x, y, p_scale=1):
        super().__init__()
        self.shoot = Auxiliar.getSurfaceFromSeparateFiles("images/npc/{0}.png", 1, 4, scale=p_scale)

        self.lives=2
        self.frame = 0
        self.image = self.shoot[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_visible = True

        self.ataque = False
        self.objetos_lanzados = pygame.sprite.Group()
        self.attack_cooldown = 2000 
        self.last_attack_time = pygame.time.get_ticks()

        self.frame_rate_ms = 200  # Ajusta este valor para ralentizar la animación

        self.tiempo_transcurrido_animation = 0

    def update(self, delta_ms):
        self.animate(delta_ms)

    def animate(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            self.frame += 1
            if self.frame >= len(self.shoot):
                self.frame = 0
            self.image = self.shoot[self.frame]
    
    def puede_atacar(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.last_attack_time
        return elapsed_time >= self.attack_cooldown

    # def lanzar_objeto(self):
    #     objeto = Objeto(self.rect.centerx, self.rect.centery, self.direction, self, p_scale=0.1)

    #     if self.direction == DIRECTION_R:
    #         objeto.velocidad_x = objeto.velocidad
    #     else:
    #         objeto.velocidad_x = -objeto.velocidad

    #     self.objetos_lanzados.add(objeto)

    def atacar(self):
        if self.puede_atacar():
            self.ataque = True
            # self.lanzar_objeto()
            self.last_attack_time = pygame.time.get_ticks()

    def draw(self, screen):
        if self.is_visible:
            screen.blit(self.image, self.rect)

    def receive_shoot(self):
        self.kill()
        self.lives-=1
        print(self.lives)
        self.is_visible = False


