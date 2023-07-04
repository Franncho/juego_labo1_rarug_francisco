import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from objeto import *

flags = DOUBLEBUF

frutas = pygame.sprite.Group()
vidas_extra=pygame.sprite.Group()  # Crear el grupo de sprites para las frutas

trampa=pygame.sprite.Group()
enemigos=pygame.sprite.Group()

pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
clock = pygame.time.Clock()

score_timer = 0

imagen_fondo = pygame.image.load("images/locations/set_bg_01/forest/robot_background.jpg").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

player_1 = Player(x=0, y=400, speed_walk=6, speed_run=12, gravity=14, jump_power=30, frame_rate_ms=100, move_rate_ms=50, jump_height=140, p_scale=0.2, interval_time_jump=300, frutas=frutas, vidas_extra=vidas_extra, trampas=trampa, enemigos=enemigos)

enemy_list=[]
enemy_list.append(Enemy(x=500, y=400, speed_walk=6, speed_run=8, gravity=8, frame_rate_ms=50, move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
enemy_list.append(Enemy(x=900, y=400, speed_walk=6, speed_run=8, gravity=8, frame_rate_ms=50, move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
enemigos.add(enemy_list)

plataform_list = []
plataform_list.append(Plataform(x=400, y=500, width=50, height=50, type=0))
plataform_list.append(Plataform(x=450, y=500, width=50, height=50, type=1))
plataform_list.append(Plataform(x=500, y=500, width=50, height=50, type=1))
plataform_list.append(Plataform(x=600, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=650, y=430, width=50, height=50, type=4))
plataform_list.append(Plataform(x=750, y=360, width=50, height=50, type=10))
plataform_list.append(Plataform(x=800, y=360, width=50, height=50, type=11))
plataform_list.append(Plataform(x=850, y=360, width=50, height=50, type=12))
plataform_list.append(Plataform(x=930, y=230, width=50, height=50, type=13))
plataform_list.append(Plataform(x=980, y=230, width=50, height=50, type=13))
plataform_list.append(Plataform(x=1150, y=120, width=50, height=50, type=13))
plataform_list.append(Plataform(x=1050, y=120, width=50, height=50, type=13))
plataform_list.append(Plataform(x=1100, y=120, width=50, height=50, type=13))


trampas = Trampa(450, 450, "C:/Users/rarug/Desktop/Rarug Francisco- Juego-python/Juego/images/Object/trampas/Spike.png", 0.2)
trampas_acid = Trampa(450, 550, "C:/Users/rarug/Desktop/Rarug Francisco- Juego-python/Juego/images/Object/trampas/Acid (1).png", 0.2)
trampa.add(trampas)
trampa.add(trampas_acid)

fruta_posiciones = [(1115, 90), (510, 470), (1115, 500)]  
for posicion in fruta_posiciones:
    x = posicion[0]
    y = posicion[1]
    fruta = Fruit(x, y, "C:/Users/rarug/Desktop/Rarug Francisco- Juego-python/Juego/images/Object/coin/1.png", scale=1)
    frutas.add(fruta)

vidas_extra_posiciones = [(1000, 90), (300, 470), (900, 500)]  
for posicion in vidas_extra_posiciones:
    x = posicion[0]
    y = posicion[1]
    vidas_extras = Fruit(x, y, "C:/Users/rarug/Desktop/Rarug Francisco- Juego-python/Juego/images/Object/hearts/1.png", scale=1)
    vidas_extra.add(vidas_extras)


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

    for enemy in enemy_list:
        enemy.update(delta_ms, plataform_list)
        enemy.draw(screen)

    for obj in frutas:
        obj.update(delta_ms)
        rotated_image = pygame.transform.rotate(obj.image, obj.angle)
        rotated_rect = rotated_image.get_rect(center=obj.rect.center)
        screen.blit(rotated_image, rotated_rect)
    
    for heart in vidas_extra:
        heart.update(delta_ms)
        rotated_image = pygame.transform.rotate(heart.image, heart.angle)
        rotated_rect = rotated_image.get_rect(center=heart.rect.center)
        screen.blit(rotated_image, rotated_rect)

    if score_timer >= 2000: 
        player_1.score += 2
        score_timer = 0  

    player_1.events(delta_ms, keys)
    player_1.update(delta_ms, plataform_list)
    player_1.draw(screen)

    player_1.objetos_lanzados.update()
    player_1.objetos_lanzados.draw(screen)

    trampa.draw(screen)

    font=pygame.font.SysFont("comicsans", 30, True)

    score_text = font.render("Score: " + str(player_1.score), True, (255, 255, 255))
    screen.blit(score_text, (600, 10))

    pygame.display.flip()





