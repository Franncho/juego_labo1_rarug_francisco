import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from objeto import *
from trampas import *
from poderes import *
from enemigo2 import *

flags = DOUBLEBUF

contador=0
estrella = pygame.sprite.Group()
# vidas_extra=pygame.sprite.Group()  # Crear el grupo de sprites para las estrella
poder = pygame.sprite.Group()

trampa=pygame.sprite.Group()
enemigos=pygame.sprite.Group()
proyectiles_enemigos=pygame.sprite.Group()
enemigo2=pygame.sprite.Group()

pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
clock = pygame.time.Clock()

score_timer = 0

#Icono y titulo
pygame.display.set_caption("Chano")
icono=pygame.image.load("images/caracters/players/robot/Idle (1).png")
pygame.display.set_icon(icono)

imagen_fondo = pygame.image.load("images/locations/set_bg_01/forest/robot_background.jpg").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

player_1 = Player(x=0, y=500, speed_walk=6, speed_run=12, gravity=10, jump_power=30, frame_rate_ms=100, move_rate_ms=50, jump_height=100, p_scale=0.2, interval_time_jump=300, estrella=estrella, poderes=poder, trampas=trampa, enemigos=enemigos, enemigo_2=enemigo2, proyectiles_enemigos=proyectiles_enemigos)

enemy_list=[]
enemy_list.append(Enemy(x=300, y=330, speed_walk=6, speed_run=8, gravity=4, frame_rate_ms=50, move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
enemy_list.append(Enemy(x=950, y=330, speed_walk=6, speed_run=8, gravity=4, frame_rate_ms=50, move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
enemigos.add(enemy_list)

enemy_2=Enemy_2(x=900, y=175, p_scale=1)
enemigo2.add(enemy_2)

plataform_list = []

plataform_list.append(Plataform(x=1100, y=500, width=50, height=50, type=13))


plataform_list.append(Plataform(x=450, y=430, width=50, height=50, type=1))
plataform_list.append(Plataform(x=500, y=430, width=50, height=50, type=1))
plataform_list.append(Plataform(x=550, y=430, width=50, height=50, type=1))


plataform_list.append(Plataform(x=650, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=700, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=750, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=800, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=850, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=900, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=950, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=1000, y=430, width=50, height=50, type=4))



plataform_list.append(Plataform(x=0, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=50, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=100, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=150, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=200, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=250, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=300, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=350, y=430, width=50, height=50, type=4))


plataform_list.append(Plataform(x=150, y=300, width=50, height=50, type=13))


plataform_list.append(Plataform(x=500, y=230, width=50, height=50, type=13))
plataform_list.append(Plataform(x=450, y=230, width=50, height=50, type=13))
plataform_list.append(Plataform(x=400, y=230, width=50, height=50, type=13))
plataform_list.append(Plataform(x=350, y=230, width=50, height=50, type=13))
plataform_list.append(Plataform(x=300, y=230, width=50, height=50, type=13))
plataform_list.append(Plataform(x=250, y=230, width=50, height=50, type=13))


plataform_list.append(Plataform(x=730, y=230, width=50, height=50, type=13))
plataform_list.append(Plataform(x=780, y=230, width=50, height=50, type=13))
plataform_list.append(Plataform(x=830, y=230, width=50, height=50, type=13))
plataform_list.append(Plataform(x=880, y=230, width=50, height=50, type=13))
plataform_list.append(Plataform(x=930, y=230, width=50, height=50, type=13))
plataform_list.append(Plataform(x=980, y=230, width=50, height=50, type=13))


plataform_list.append(Plataform(x=1150, y=120, width=50, height=50, type=13))
plataform_list.append(Plataform(x=1050, y=120, width=50, height=50, type=13))
plataform_list.append(Plataform(x=1100, y=120, width=50, height=50, type=13))


trampas = Trampa(500, 380, "images/Object/trampas/Spike.png", 0.2)
trampa.add(trampas)


star_list = [(115, 360), (300, 170), (1115, 60)]  
for posicion in star_list:
    x = posicion[0]
    y = posicion[1]
    star= Poderes(x, y, "images/Object/coin/star.png", scale=0.3)
    estrella.add(star)

# vidas_extra_posiciones = [(1000, 90), (300, 470), (900, 500)]  
# for posicion in vidas_extra_posiciones:
#     x = posicion[0]
#     y = posicion[1]
#     vidas_extras = Fruit(x, y, "images/Object/hearts/heart.png", scale=0.2)
#     vidas_extra.add(vidas_extras)


poderes = [(250, 170)]  
for posicion in poderes:
    x = posicion[0]
    y = posicion[1]
    poderes = Poderes(x, y, "images/Object/coin/papas.png", scale=2)
    poder.add(poderes)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)
    score_timer += delta_ms
    
    screen.blit(imagen_fondo, (0, 0))

    for plataforma in plataform_list:
        plataforma.draw(screen)

    for index, enemy in enumerate(enemy_list):
        enemy.update(delta_ms, plataform_list, enemy_list, index)
        enemy.draw(screen)

        if enemy.puede_atacar():
            enemy.atacar()

    for obj in estrella:
        obj.update(delta_ms)
        rotated_image = pygame.transform.rotate(obj.image, obj.angle)
        rotated_rect = rotated_image.get_rect(center=obj.rect.center)
        screen.blit(rotated_image, rotated_rect)
    
    # for heart in vidas_extra:
    #     heart.update(delta_ms)
    #     rotated_image = pygame.transform.rotate(heart.image, heart.angle)
    #     rotated_rect = rotated_image.get_rect(center=heart.rect.center)
    #     screen.blit(rotated_image, rotated_rect)


    for i in poder:
        i.update(delta_ms)
        rotated_image = pygame.transform.rotate(i.image, i.angle)
        rotated_rect = rotated_image.get_rect(center=i.rect.center)
        screen.blit(rotated_image, rotated_rect)
    
    if player_1.lives > 0:
        if score_timer >= 2000: 
            player_1.score += 2
            score_timer = 0  
    
    if player_1.game_over and player_1.is_death_animation_finished==True:
             for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player_1 = Player(x=0, y=500, speed_walk=6, speed_run=12, gravity=10, jump_power=30, frame_rate_ms=100, move_rate_ms=50, jump_height=100, p_scale=0.2, interval_time_jump=300, estrella=estrella, poderes=poder, trampas=trampa, enemigos=enemigos, enemigo_2=enemigo2, proyectiles_enemigos=proyectiles_enemigos)
                    enemy_list=[]
                    enemy_list.append(Enemy(x=300, y=330, speed_walk=6, speed_run=8, gravity=4, frame_rate_ms=50, move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
                    enemy_list.append(Enemy(x=950, y=330, speed_walk=6, speed_run=8, gravity=4, frame_rate_ms=50, move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
                    enemigos.add(enemy_list)

                    enemy_2=Enemy_2(x=900, y=175, p_scale=1)
                    enemigo2.add(enemy_2)

    player_1.events(delta_ms, keys)
    player_1.update(delta_ms, plataform_list, player_1, index)
    player_1.draw(screen)
    enemy_2.draw(screen)
    enemy_2.update(delta_ms)

    player_1.objetos_lanzados.update()
    player_1.objetos_lanzados.draw(screen)

    

    trampa.draw(screen)

    font_score=pygame.font.SysFont("comicsans", 20, True)
    font=pygame.font.SysFont("arial", 20, True)

    score_text = font_score.render("Score: " + str(player_1.score), True, (255, 255, 255))
    screen.blit(score_text, (600, 5))

    lives_text = font.render("Lives:", True, (255, 255, 255))
    screen.blit(lives_text, (10, 5))

    stars_text = font.render("Stars:", True, (255, 255, 255))
    screen.blit(stars_text, (300, 5))

    pygame.display.flip()





