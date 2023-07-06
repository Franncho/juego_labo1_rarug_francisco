import pygame
from constantes import *
from auxiliar import Auxiliar
from objeto import *
from enemigo import *
from enemigo2 import *

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100,estrella=None, poderes=None, trampas=None, enemigos=None, enemigo_2=None, proyectiles_enemigos=None) -> None:
        '''
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,scale=p_scale)[:12]
        '''

        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Idle ({0}).png",1,10,flip=False,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Idle ({0}).png",1,10,flip=True,scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Jump ({0}).png",1,10,flip=True,scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Jump ({0}).png",1,10,flip=False,scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Run ({0}).png",1,8,flip=False,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Run ({0}).png",1,8,flip=True,scale=p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Shoot ({0}).png",1,4,flip=False,scale=p_scale,repeat_frame=2)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Shoot ({0}).png",1,4,flip=True,scale=p_scale,repeat_frame=2)
        self.knife_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Melee ({0}).png",1,7,flip=False,scale=p_scale,repeat_frame=1)
        self.knife_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Melee ({0}).png",1,8,flip=True,scale=p_scale,repeat_frame=1)
        self.dead_r=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Dead ({0}).png", 1,10,flip=False,scale=p_scale,repeat_frame=1)
        self.dead_l=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Dead ({0}).png", 1,10,flip=True,scale=p_scale,repeat_frame=1)
        self.is_dead = False

        self.frame = 0
        self.lives = 3
        self.estrella = estrella
        # self.vidas_extra=vidas_extra
        self.poderes=poderes
        self.trampas=trampas
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.topleft = (self.rect.x, self.rect.y)
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

        self.objetos_lanzados = pygame.sprite.Group()
        self.attack_launched = False
        self.heat_state=False
        self.delta = 0
        self.is_death_animation_finished = False
        self.game_over=False
        self.restart_game = True
        self.mask = pygame.mask.from_surface(self.image)
        self.enemigos=enemigos
        self.enemigo_2=enemigo_2
        self.proyectiles_enemigos=proyectiles_enemigos

        

    def walk(self,direction):
        if self.is_dead:
            return
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

    def shoot(self,on_off = True):
        if self.is_dead:
            return
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):

            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l       

    def receive_shoot(self):
        self.lives -= 1

    def knife(self,on_off = True):
        if self.is_dead:
            return
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                else:
                    self.animation = self.knife_l      

    def jump(self,on_off = True):
        if self.is_dead:
            return
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if self.is_dead:
            return
        if(self.is_knife or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        if self.is_dead:
            return
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False            

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

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0

    def lanzar_objeto(self):
        objeto = Objeto(self.rect.centerx, self.rect.centery, self.direction, self, p_scale=0.1)

        if self.direction == DIRECTION_R:
            objeto.velocidad_x = objeto.velocidad
        else:
            objeto.velocidad_x = -objeto.velocidad

        self.objetos_lanzados.add(objeto)



    def draw_hearts(self, screen, scale):
        heart_image = pygame.image.load("images/Object/hearts/heart.png")
        heart_width = heart_image.get_width() * scale
        heart_height = heart_image.get_height() * scale
        spacing = 10  # Espacio entre los corazones
        x = 70  # Posición x inicial
        y = 10  # Posición y
        for _ in range(self.lives):
            heart_scaled = pygame.transform.scale(heart_image, (heart_width, heart_height))
            screen.blit(heart_scaled, (x, y))
            x += heart_width + spacing

    
    def draw_star(self, screen, scale):
        if self.estrella:  # Verificar si la lista no está vacía
            star_image = pygame.image.load("images/Object/coin/star.png")
            star_width = star_image.get_width() * scale
            star_height = star_image.get_height() * scale
            spacing = 10  # Espacio entre las estrellas
            x = 360  # Posición x inicial
            y = 7  # Posición y
            for _ in self.estrella:
                star_scaled = pygame.transform.scale(star_image, (star_width, star_height))
                screen.blit(star_scaled, (x, y))
                x += star_width + spacing

    def check_collision(self):
        for trampa in self.trampas:
            if not self.heat_state:
                if pygame.sprite.collide_mask(self,trampa):
                    self.delta = pygame.time.get_ticks()
                    self.lives -= 1
                    self.score-=2
                    self.heat_state = True

        if self.heat_state:
            current_time = pygame.time.get_ticks()
            if current_time - self.delta > 1000:
                self.heat_state = False

    def death_animation(self):
        if self.animation != self.dead_r and self.animation != self.dead_l:
            self.frame = 0
        self.is_dead = True
        if self.direction == DIRECTION_R:
            self.animation = self.dead_r
        else:
            self.animation = self.dead_l
        if self.frame == len(self.animation) - 1:
            self.is_death_animation_finished = True
            self.game_over = True
    
    def recibir_ataque(self):
        self.vida -= 1
        if self.vida <= 0:
            self.game_over = True

    def update(self, delta_ms, plataform_list):
            if not self.game_over:

                self.do_movement(delta_ms, plataform_list)
                self.do_animation(delta_ms)
                self.check_collision()

                if not self.heat_state:
                    self.delta = delta_ms

                colisiones_coin = pygame.sprite.spritecollide(self, self.estrella, True)
                if colisiones_coin:
                    self.score += 10
                    print(self.score)

                colisiones_poderes = pygame.sprite.spritecollide(self, self.poderes, True)
                if colisiones_poderes:
                    self.jump_height += 100
                    print(self.jump_height)

                if self.lives==0:
                    self.death_animation() 

                for objeto in self.objetos_lanzados:
                    colisiones_enemigos = pygame.sprite.spritecollide(objeto, self.enemigos, False)
                    if colisiones_enemigos:
                        for enemigos in colisiones_enemigos:
                            enemigos.receive_shoot(self.enemigos)
                            self.score+=3
                            self.attack_launched = False
                            objeto.kill()
                
                for objeto in self.objetos_lanzados:
                    colisiones_enemigos_2 = pygame.sprite.spritecollide(objeto, self.enemigo_2, False)
                    if colisiones_enemigos_2:
                        for enemigos in colisiones_enemigos_2:
                            enemigos.receive_shoot()
                            self.score+=3
                            self.attack_launched = False
                            objeto.kill()

                colisiones_proyectiles = pygame.sprite.spritecollide(self, self.proyectiles_enemigos, True)
                if colisiones_proyectiles:
                    self.recibir_ataque()
                
                self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
                self.mask = pygame.mask.from_surface(self.image)


    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        if not self.game_over:
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
            
            self.draw_hearts(screen, 0.1)

            colisiones_star = pygame.sprite.spritecollide(self, self.estrella, True)
            if colisiones_star:
                self.draw_star(screen, 0.2)
                self.estrella+=1

        if self.game_over:
            font=pygame.font.SysFont("serif", 25)
            text=font.render("Game Over", "Hace click para continuar", True, C_BLUE)
            center_x=(ANCHO_VENTANA//2) - (text.get_width()//2)
            center_y=(ALTO_VENTANA//2) - (text.get_height()//2)
            screen.blit(text, [center_x, center_y])

    def events(self,delta_ms,keys):
        self.tiempo_transcurrido += delta_ms


        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

        if(not keys[pygame.K_x]):
            self.shoot(False)  

        if(not keys[pygame.K_x]):
            self.knife(False)  

        if(keys[pygame.K_z] and not keys[pygame.K_x] and not self.attack_launched):
            self.shoot()
            self.lanzar_objeto()
            self.attack_launched = True
        
        if(keys[pygame.K_x] and not keys[pygame.K_z]):
            self.knife()
        
        # if self.game_over and self.is_death_animation_finished==True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             self.restart_game = False
        #             self.game_over = False
        #             self.lives = 3
        #             self.score=0
        #             self.rect.x = 0
        #             self.rect.y = 400
