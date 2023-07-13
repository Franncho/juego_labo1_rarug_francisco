import pygame
from player import *
from objeto import *
from constantes import *
from auxiliar import Auxiliar

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100, numero_enemy=None) -> None:
        super().__init__()
        self.numero_enemy=numero_enemy

        if self.numero_enemy==1:
            self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/blue/run/r_{0}.png",0,6,scale=p_scale)
            self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/blue/run/r_{0}.png",0,6,flip=True,scale=p_scale)
            self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/blue/idle/i_{0}.png",0,6,scale=p_scale)
            self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/blue/idle/i_{0}.png",0,6,flip=True,scale=p_scale)
            self.dead_r=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/blue/die/d_{0}.png",0,17,scale=p_scale)
            self.dead_l=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/blue/die/d_{0}.png",0,17,flip=True,scale=p_scale)

        elif self.numero_enemy==2:
            self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/brown/run/r_{0}.png",0,6,scale=p_scale)
            self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/brown/run/r_{0}.png",0,6,flip=True,scale=p_scale)
            self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/brown/idle/i_{0}.png",0,6,scale=p_scale)
            self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/brown/idle/i_{0}.png",0,6,flip=True,scale=p_scale)
            self.dead_r=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/brown/die/d_{0}.png",0,17,scale=p_scale)
            self.dead_l=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/brown/die/d_{0}.png",0,17,flip=True,scale=p_scale)

        elif self.numero_enemy==3:
            self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/green/run/r_{0}.png",0,6,scale=p_scale)
            self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/green/run/r_{0}.png",0,6,flip=True,scale=p_scale)
            self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/green/idle/i_{0}.png",0,6,scale=p_scale)
            self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/green/idle/i_{0}.png",0,6,flip=True,scale=p_scale)
            self.dead_r=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/green/die/d_{0}.png",0,17,scale=p_scale)
            self.dead_l=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/green/die/d_{0}.png",0,17,flip=True,scale=p_scale)

        elif self.numero_enemy==4:
            self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/boss/02_demon_walk/{0}.png",0,11,flip=True,scale=p_scale)
            self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/boss/02_demon_walk/{0}.png",0,11,scale=p_scale)
            self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/boss/01_demon_idle/{0}.png",0,6,scale=p_scale)
            self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/boss/01_demon_idle/{0}.png",0,6,flip=True,scale=p_scale)
            self.dead_r=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/boss/05_demon_death/{0}.png",0,21,scale=p_scale)
            self.dead_l=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/boss/05_demon_death/{0}.png",0,21,flip=True,scale=p_scale)


        self.contador = 0
        self.frame = 0

        if self.numero_enemy==1 or self.numero_enemy==2 or self.numero_enemy==3:
            self.lives = 2
        
        if self.numero_enemy==4:
            self.lives=6
        

        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r

        if self.numero_enemy==4:
            self.direction = DIRECTION_L

        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False
        self.ataque = False

        self.objetos_lanzados = pygame.sprite.Group()
        if self.numero_enemy==1 or self.numero_enemy==2 or self.numero_enemy==3:
            self.attack_cooldown = 5000

        if self.numero_enemy==4:
            self.attack_cooldown = 3000


        self.last_attack_time = pygame.time.get_ticks()

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump
        self.is_dead = False
        self.is_visible = True
        self.death_animation_finished = False

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if self.lives>0:
            if(self.tiempo_transcurrido_move >= self.move_rate_ms):
                self.tiempo_transcurrido_move = 0

                if(not self.is_on_plataform(plataform_list)):
                    if(self.move_y == 0):
                        self.is_fall = True
                        self.change_y(self.gravity)
                else:
                    self.is_fall = False
                    self.change_x(self.move_x)
                    if self.contador <= 50:
                        self.move_x = -self.speed_walk
                        self.animation = self.walk_l
                        self.direction=DIRECTION_L
                        self.contador += 1 
                    elif self.contador <= 100:
                        self.move_x = self.speed_walk
                        self.animation = self.walk_r
                        self.direction=DIRECTION_R
                        self.contador += 1
                    else:
                        self.contador = 0
    
    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno          

    def do_animation(self,delta_ms, enemy_list, index):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            elif self.frame >= len(self.animation) - 1 :
                if self.animation==self.dead_r or self.animation==self.dead_l:
                    del enemy_list[index]
                else:
                    self.frame=0

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

    def lanzar_disparo(self):
        
        if self.numero_enemy==1:
            tiro = Objeto(self.rect.centerx, self.rect.centery, self.direction, self, p_scale=0.4, numero_objeto=1)
        if self.numero_enemy==2:
            tiro = Objeto(self.rect.centerx, self.rect.centery, self.direction, self, p_scale=0.4, numero_objeto=2)
        if self.numero_enemy==3:
            tiro = Objeto(self.rect.centerx, self.rect.centery, self.direction, self, p_scale=0.4, numero_objeto=3)
        if self.numero_enemy==4:
            tiro = Objeto(self.rect.centerx, self.rect.centery, self.direction, self, p_scale=0.4, numero_objeto=4)
        
        if self.direction == DIRECTION_R:
                tiro.velocidad_x = tiro.velocidad
        else:
            tiro.velocidad_x = -tiro.velocidad

        self.objetos_lanzados.add(tiro)

    def atacar(self, pause):
        if not pause:
            if self.puede_atacar():
                self.lanzar_disparo()
                self.last_attack_time = pygame.time.get_ticks()

    def update(self,delta_ms,plataform_list, enemy_list, index, pause):
        if not pause:
            self.do_movement(delta_ms,plataform_list)
            self.do_animation(delta_ms, enemy_list, index) 
            self.atacar(pause)

    def draw(self,screen):
        if self.is_visible and not self.death_animation_finished:
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
                pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)

    def receive_shoot(self, enemy_list):
        self.lives -= 1
        print(self.lives)

        if self.lives <= 0:
            self.lives = 0
            self.death_animation()
            enemy_list.remove(self)
        
