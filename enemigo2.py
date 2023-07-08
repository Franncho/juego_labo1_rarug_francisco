import pygame
from constantes import *
from auxiliar import Auxiliar

class Enemy_2(pygame.sprite.Sprite):
    def __init__(self, x, y, p_scale=1):
        super().__init__()


        # self.shoot= Auxiliar.getSurfaceFromSeparateFiles("images/npc/{0}.png", 1, 4, scale=p_scale)
        self.lives=2
        self.animation= Auxiliar.getSurfaceFromSeparateFiles("images/npc/{0}.png", 1, 4, scale=p_scale)
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_visible = True
        self.dead_r=Auxiliar.getSurfaceFromSpriteSheet("images/npc/die/1.png", 6, 1, scale=p_scale)[1:6]
        self.direction = DIRECTION_R
        self.ataque = False
        self.objetos_lanzados = pygame.sprite.Group()
        self.attack_cooldown = 2000 
        self.last_attack_time = pygame.time.get_ticks()
        self.is_dead = False

        self.frame_rate_ms = 200  # Ajusta este valor para ralentizar la animación

        self.tiempo_transcurrido_animation = 0

    

    def animate(self, delta_ms, enemy_list_2, index):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            self.frame += 1
            if self.frame >= len(self.animation)-1:
                if self.animation==self.dead_r:
                    del enemy_list_2[index]
                else:
                    self.frame = 0
            self.image = self.animation[self.frame]
            

    def death_animation(self):
        self.is_dead = True
        if self.direction == DIRECTION_R:
            self.animation = self.dead_r
        else:
            self.animation = self.dead_l
    
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

    def update(self, delta_ms, enemy_list_2, index):
        self.animate(delta_ms, enemy_list_2, index)

    def draw(self, screen):
        if self.is_visible:
            screen.blit(self.image, self.rect)

    def receive_shoot(self, enemy_list_2):
        self.lives -= 1
        print(self.lives)

        if self.lives <= 0:
            self.lives = 0
            self.death_animation()
            enemy_list_2.remove(self)


