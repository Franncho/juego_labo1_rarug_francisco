import pygame
from constantes import *
from auxiliar import Auxiliar
from objeto import *
from trampas import *
from poderes import *
from enemigo import *
from enemigo2 import *
from plataforma_movil import *


class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100,estrella=None, poderes=None, vidas_extra=None, trampas=None, enemigos=None, enemigo_2=None, numero_player=None) -> None:
        
        self.numero_player=numero_player
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Idle ({0}).png",1,10,flip=False,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Idle ({0}).png",1,10,flip=True,scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Jump ({0}).png",1,10,flip=True,scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Jump ({0}).png",1,10,flip=False,scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Run ({0}).png",1,8,flip=False,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Run ({0}).png",1,8,flip=True,scale=p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Shoot ({0}).png",1,4,flip=False,scale=p_scale,repeat_frame=2)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Shoot ({0}).png",1,4,flip=True,scale=p_scale,repeat_frame=2)
        self.dead_r=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Dead ({0}).png", 1,10,flip=False,scale=p_scale,repeat_frame=1)
        self.dead_l=Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/robot/Dead ({0}).png", 1,10,flip=True,scale=p_scale,repeat_frame=1)
        self.is_dead = False

        self.frame = 0
        self.lives = 5
        self.estrella = estrella
        self.vidas_extra=vidas_extra
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

        self.win=False
        self.poder_salto_time = 0
        self.last_power_collected_time = 0
        self.contador_estrella=0
        self.pause=False

        self.invulnerable = False  # Variable de estado de invulnerabilidad
        self.invulnerable_timer = 0  # Temporizador de invulnerabilidad
        self.invulnerable_duration = 600  # Duración en milisegundos de la invulnerabilidad

        self.max_limit=ANCHO_VENTANA

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
        if(self.is_shoot):
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

    def check_ground_collision(self, plataform_list):
        for plataforma in plataform_list:
            if self.ground_collition_rect.colliderect(plataforma.ground_collition_rect):
                self.rect.bottom = plataforma.ground_collition_rect.top
                self.collition_rect.bottom = self.rect.bottom
                self.ground_collition_rect.bottom = self.collition_rect.bottom
                break

    def do_movement(self, delta_ms, plataform_list, plataforma_movil_lista ):
        if self.is_dead:
            return
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            self.tiempo_transcurrido_move = 0

            if abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump:
                self.move_y = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if not self.is_on_plataform(plataform_list,  plataforma_movil_lista):
                if self.move_y == 0:
                    self.is_fall = True
                    self.change_y(self.gravity)
                else:
                    self.is_fall = False
                    self.check_ground_collision(plataform_list)
            else:
                if self.is_jump:
                    self.jump(False)
                self.is_fall = False

    def is_on_plataform(self,plataform_list, plataforma_movil_lista):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True 

        else:
            if plataforma_movil_lista:
                for plataforma_movil in plataforma_movil_lista:
                    if self.ground_collition_rect.colliderect(plataforma_movil.collision_rect):
                        return True 
            for plataforma in plataform_list:
                if self.ground_collition_rect.colliderect(plataforma.ground_collition_rect):
                    return True      
        return retorno                 

    def do_animation(self,delta_ms, player, index):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            elif self.frame >= len(self.animation) - 1 :
                if self.animation==self.dead_r or self.animation==self.dead_l:
                    del player[index]
                else:
                    self.frame=0

    def lanzar_objeto(self):
        if not self.pause:

            objeto = Objeto(self.rect.centerx, self.rect.centery, self.direction, self, p_scale=0.5, numero_objeto=1)

            if self.direction == DIRECTION_R:
                objeto.velocidad_x = objeto.velocidad
            else:
                objeto.velocidad_x = -objeto.velocidad

            self.objetos_lanzados.add(objeto)

    def draw_hearts(self, screen, scale):
        heart_image = pygame.image.load("images/Object/hearts/heart.png")
        heart_width = heart_image.get_width() * scale
        heart_height = heart_image.get_height() * scale
        spacing = 10
        x = 70  
        y = 10  
        for _ in range(self.lives):
            heart_scaled = pygame.transform.scale(heart_image, (heart_width, heart_height))
            screen.blit(heart_scaled, (x, y))
            x += heart_width + spacing

    def draw_star(self, screen, scale):
        star_image = pygame.image.load("images/Object/coin/star.png")
        star_width = star_image.get_width() * scale
        star_height = star_image.get_height() * scale
        spacing = 10 
        x = 360 
        y = 5 
        for _ in range(len(self.estrella)):
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
                    sonido_colision = pygame.mixer.Sound("audio/daño.wav")
                    volumen = 0.2 
                    sonido_colision.set_volume(volumen)
                    sonido_colision.play()

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
        if not self.invulnerable:

            self.lives -= 1
            self.frame = 0
            self.recibe_hurt = True
            self.invulnerable = True 
            self.invulnerable_timer = pygame.time.get_ticks() 

            sonido_colision = pygame.mixer.Sound("audio/daño.wav")
            volumen = 0.2 
            sonido_colision.set_volume(volumen)
            sonido_colision.play()

        if self.lives <= 0:
            self.lives = 0
            self.death_animation()

            sonido_colision = pygame.mixer.Sound("audio/dead.wav")
            volumen = 0.2 
            sonido_colision.set_volume(volumen)
            sonido_colision.play()
            # self.remove(self)

    
    def update(self, delta_ms, plataform_list, player, index, enemy_list, enemy_list_2,  plataforma_movil_lista):
            if not self.pause and not self.game_over:
                self.do_movement(delta_ms, plataform_list, plataforma_movil_lista)
                self.do_animation(delta_ms, player, index)
                self.check_collision()


                if not self.heat_state:
                    self.delta = delta_ms

                colisiones_coin = pygame.sprite.spritecollide(self, self.estrella, True)
                if colisiones_coin:
                    self.score += 10
                    self.contador_estrella+=1
                    print(self.score)
                    sonido_colision = pygame.mixer.Sound("audio/coin.wav")
                    volumen = 0.2 
                    sonido_colision.set_volume(volumen)
                    sonido_colision.play()

                if self.numero_player==1:
                    colisiones_poderes = pygame.sprite.spritecollide(self, self.poderes, True)
                    if colisiones_poderes:
                        self.poder_salto_time = pygame.time.get_ticks()
                        self.jump_height += 100

                        sonido_colision = pygame.mixer.Sound("audio/objeto.wav")
                        volumen = 0.2 
                        sonido_colision.set_volume(volumen)
                        sonido_colision.play()

                    current_time = pygame.time.get_ticks()
                    if current_time - self.poder_salto_time >= 3000:
                        self.jump_height = 100
                    
                    if current_time - self.last_power_collected_time >= 5000:  # 5 segundos en milisegundos
                        self.poderes.empty()
                        # Crear nuevo poder
                        new_power = Poderes(250, 170, "images/Object/coin/papas.png", scale=2)
                        self.poderes.add(new_power)
                        self.last_power_collected_time = current_time

                
                if self.numero_player==3:
                    colisiones_vidas = pygame.sprite.spritecollide(self, self.vidas_extra, True)
                    if colisiones_vidas:
                        self.lives += 1
                        sonido_colision = pygame.mixer.Sound("audio/coin.wav")
                        volumen = 0.2 
                        sonido_colision.set_volume(volumen)
                        sonido_colision.play()


                if self.lives==0:
                    self.death_animation()
                    sonido_colision = pygame.mixer.Sound("audio/dead.wav")
                    volumen = 0.2 
                    sonido_colision.set_volume(volumen)
                    sonido_colision.play()

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
                            enemigos.receive_shoot(self.enemigo_2)
                            self.score+=3
                            self.attack_launched = False
                            objeto.kill()

                for enemy in enemy_list:
                    for objeto in enemy.objetos_lanzados:
                        if self.collition_rect.colliderect(objeto.rect):
                            self.recibir_ataque()
                
                for enemy_2 in enemy_list_2:
                    for objeto in enemy_2.objetos_lanzados:
                        if self.collition_rect.colliderect(objeto.rect):
                            self.recibir_ataque()
                            objeto.remove()

                if self.numero_player==3:
                    collision_enemy = pygame.sprite.spritecollide(self, self.enemigos, False)
                    if collision_enemy:
                        for enemy in collision_enemy:
                            self.lives -= 1
                            print(self.lives)
                            push_direction = pygame.Vector2(self.rect.center) - pygame.Vector2(enemy.rect.center)
                            push_direction.normalize_ip()
                            push_force = push_direction * 50 
                            self.collition_rect.move_ip(push_force)
                            self.rect.move_ip(push_force)
                            self.ground_collition_rect.move_ip(push_force)

                            sonido_colision = pygame.mixer.Sound("audio/daño.wav")
                            volumen = 0.2 
                            sonido_colision.set_volume(volumen)
                            sonido_colision.play()
                
                collision_enemy_2 = pygame.sprite.spritecollide(self, self.enemigo_2, False)
                if collision_enemy_2:
                    for enemy_2 in collision_enemy_2:
                        self.lives -= 1
                        print(self.lives)
                        push_direction = pygame.Vector2(self.rect.center) - pygame.Vector2(enemy_2.rect.center)
                        push_direction.normalize_ip()
                        push_force = push_direction * 50  # Ajusta la magnitud del empuje según sea necesario
                        self.collition_rect.move_ip(push_force)
                        self.rect.move_ip(push_force)
                        self.ground_collition_rect.move_ip(push_force)

                        sonido_colision = pygame.mixer.Sound("audio/daño.wav")
                        volumen = 0.2 
                        sonido_colision.set_volume(volumen)
                        sonido_colision.play()

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
            self.draw_star(screen, 0.2)
        
        if self.contador_estrella>=3:
            self.win=True
            self.pause=True

            sonido_colision = pygame.mixer.Sound("audio/win.wav")
            volumen = 0.2 
            sonido_colision.set_volume(volumen)
            sonido_colision.play()

    def events(self,delta_ms,keys): 
        self.tiempo_transcurrido += delta_ms

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not self.pause):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not self.pause):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not self.pause):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not self.pause):
            self.stay()  

        if(keys[pygame.K_SPACE] and not self.pause):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

                sonido_colision = pygame.mixer.Sound("audio/jump.wav")
                volumen = 0.2 
                sonido_colision.set_volume(volumen)
                sonido_colision.play()

        if(not keys[pygame.K_x] and not self.pause):
            self.shoot(False)  

        if(keys[pygame.K_z] and not keys[pygame.K_x] and not self.attack_launched and not self.pause):
            self.shoot()
            self.lanzar_objeto()
            self.attack_launched = True

            sonido_colision = pygame.mixer.Sound("audio/disparo.wav")
            volumen = 0.2 
            sonido_colision.set_volume(volumen)
            sonido_colision.play()
        
        if(keys[pygame.K_ESCAPE]):
            self.pause=True
