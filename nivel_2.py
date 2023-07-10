import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from enemigo import *
from plataforma import Plataform
from objeto import *
from trampas import *
from poderes import *
from enemigo2 import *
from comienzo import *
from main import *
from plataforma_movil import *


flags = DOUBLEBUF



# Inicio.comienzo()

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

#Icono y titulo
pygame.display.set_caption("Chano")
icono=pygame.image.load("images/caracters/players/robot/Idle (1).png")
pygame.display.set_icon(icono)

#Se inicializa la imagen del fondo y se escala al alto y ancho de la pantalla
imagen_fondo = pygame.image.load("images/locations/set_bg_01/forest/background_2.jpg").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

def nivel_2():
    from nivel_3 import nivel_3
    from main import main
    #Creacion de grupo de sprites para colisiones
    estrella = pygame.sprite.Group()
    poder = pygame.sprite.Group()
    trampa=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    enemigo2=pygame.sprite.Group()
    plataform=pygame.sprite.Group()

    #Variables varias
    score_timer = 0
    contador_estrellas=0

    #Inicializar el personaje 1 con sus atributos correspondientes
    player_1 = Player(x=0, y=0, speed_walk=12, speed_run=24, gravity=10, jump_power=30, frame_rate_ms=100, move_rate_ms=50, jump_height=100, p_scale=0.2, interval_time_jump=300, estrella=estrella, poderes=poder, trampas=trampa, enemigos=enemigos, enemigo_2=enemigo2)

    #Inicializar los enemigos con sus atributos correspondientes
    enemy_list=[]
    enemy_list.append(Enemy(x=300, y=330, speed_walk=6, speed_run=8, gravity=4, frame_rate_ms=50, move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
    enemy_list.append(Enemy(x=1100, y=330, speed_walk=6, speed_run=8, gravity=4, frame_rate_ms=50, move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
    enemigos.add(enemy_list)

    enemy_list_2=[]
    enemy_list_2.append(Enemy_2(x=100, y=65, p_scale=1))
    enemigo2.add(enemy_list_2)

    #Declaracion de plataformas
    plataform_list = []

    plataform_list.append(Plataform(x=0, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=50, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=100, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=150, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=200, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=250, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=300, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=350, y=500, width=50, height=50, type=4))

    plataform_list.append(Plataform(x=800, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=850, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=900, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=950, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=1000, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=1050, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=1100, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=1150, y=500, width=50, height=50, type=4))
    plataform_list.append(Plataform(x=1200, y=500, width=50, height=50, type=4))

    # plataform_list.append(Plataform(x=150, y=300, width=50, height=50, type=13))

    plataform_list.append(Plataform(x=0, y=120, width=50, height=50, type=13))
    plataform_list.append(Plataform(x=50, y=120, width=50, height=50, type=13))
    plataform_list.append(Plataform(x=100, y=120, width=50, height=50, type=13))



    plataform_list.append(Plataform(x=595, y=120, width=50, height=50, type=13))
    

    plataform_list.append(Plataform(x=1050, y=120, width=50, height=50, type=13))
    plataform_list.append(Plataform(x=1150, y=120, width=50, height=50, type=13))

    plataform.add(plataform_list)

    plataforma_movil_lista=[]
    plataforma_movil_lista.append(PlataformaMovil(400, 500, 100, 50, 50, 0.01, movimiento=0, type=4))

    plataforma_movil_lista_2=[]
    plataforma_movil_lista_2.append(PlataformaMovil(645, 120, 100, 50, 50, 0.01, movimiento=0, type=13))

    plataforma_movil_lista_3=[]
    plataforma_movil_lista_3.append(PlataformaMovil(150, 120, 100, 50, 50, 0.01, movimiento=0, type=13))

    plataforma_movil_lista_4=[]
    plataforma_movil_lista_4.append(PlataformaMovil(1100, 120, 90, 50, 50, 0.01, movimiento=1, type=13))

    #Declaracion y aplicacion de las trampas
    trampas_list=[]


    trampas_list.append(Trampa(0, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(50, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(100, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(150, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(200, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(250, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(300, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(350, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(400, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(450, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(500, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(550, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(600, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(650, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(700, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(750, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(800, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(850, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(900, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(950, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1000, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1050, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1100, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1050, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1100, 550, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1150, 550, "images/Object/trampas/Acid (1).png", 0.2))


    trampas_list.append(Trampa(0, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(50, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(100, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(150, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(200, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(250, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(300, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(350, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(400, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(450, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(500, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(550, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(600, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(650, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(700, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(750, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(800, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(850, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(900, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(950, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1000, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1050, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1100, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1050, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1100, 570, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1150, 570, "images/Object/trampas/Acid (1).png", 0.2))

    trampas_list.append(Trampa(0, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(50, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(100, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(150, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(200, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(250, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(300, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(350, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(400, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(450, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(500, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(550, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(600, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(650, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(700, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(750, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(800, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(850, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(900, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(950, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1000, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1050, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1100, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1050, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1100, 600, "images/Object/trampas/Acid (1).png", 0.2))
    trampas_list.append(Trampa(1150, 600, "images/Object/trampas/Acid (1).png", 0.2))

    trampas_list.append(Trampa(700, 600, "images/Object/trampas/Acid (1).png", 0.2))

    # trampas_list.append(Trampa(500, 380, "images/Object/trampas/Spike.png", 0.2))

    trampa.add(trampas_list)

    #Declaracion y aplicacion de las estrellas
    star_list = [(600, 80), (50, 80), (1100, 400)]  
    for posicion in star_list:
        x = posicion[0]
        y = posicion[1]
        star= Poderes(x, y, "images/Object/coin/star.png", scale=0.3)
        estrella.add(star)

    #Declaracion y aplicacion de los poderes
    poderes = [(250, 170)]  
    for posicion in poderes:
        x = posicion[0]
        y = posicion[1]
        poderes = Poderes(x, y, "images/Object/coin/papas.png", scale=2)
        poder.add(poderes)


    def reset_objects():
        estrella.empty()
        poder.empty()

        star_list = [(115, 360), (300, 170), (1115, 60)]
        for posicion in star_list:
            x = posicion[0]
            y = posicion[1]
            star = Poderes(x, y, "images/Object/coin/star.png", scale=0.3)
            estrella.add(star)

        poderes = [(250, 170)]
        for posicion in poderes:
            x = posicion[0]
            y = posicion[1]
            poder_objeto = Poderes(x, y, "images/Object/coin/papas.png", scale=2)
            poder.add(poder_objeto)

        
    def draw_star(self, screen, scale):
        '''
        Dibuja las estrellas correspondientes a los objetos recolectados por el jugador en la pantalla.

        Parámetros:
        - screen (objeto pygame.Surface): Superficie de la pantalla donde se dibujan las estrellas.
        - scale (float): Factor de escala para el tamaño de las estrellas.
        '''
        star_image = pygame.image.load("images/Object/coin/star.png")
        star_width = star_image.get_width() * scale
        star_height = star_image.get_height() * scale
        spacing = 10  # Espacio entre los corazones
        x = 360  # Posición x inicial
        y = 10  # Posición y
        for _ in range(self.estrella):
            star_scaled = pygame.transform.scale(star_image, (star_width, star_height))
            screen.blit(star_scaled, (x, y))
            x += star_width + spacing

        

    #Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if marco_1_rect.collidepoint(event.pos):
                    nivel_2()
                elif marco_2_rect.collidepoint(event.pos):
                    main()
                elif marco_3_rect.collidepoint(event.pos):
                    player_1.pause=False


                elif nivel_1_rect_win.collidepoint(event.pos):
                    nivel_2()
                elif nivel_2_rect_win.collidepoint(event.pos):
                    nivel_3()
                elif nivel_3_rect_win.collidepoint(event.pos):
                    main()
            


        keys = pygame.key.get_pressed()
        if not player_1.pause:
            delta_ms = clock.tick(FPS)
            score_timer += delta_ms
        
        #Declaracion del fondo del juego
        screen.blit(imagen_fondo, (0, 0))

        #Dibujas en pantalla objetos variados
        for plataforma in plataform_list:
            plataforma.draw(screen)

        for index, enemy in enumerate(enemy_list):
            enemy.update(delta_ms, plataform_list, enemy_list, index, pause=player_1.pause)
            enemy.draw(screen)

            if not player_1.pause:
                enemy.objetos_lanzados.update()
            enemy.objetos_lanzados.draw(screen)

        for index, enemy_2 in enumerate(enemy_list_2):
            enemy_2.update(delta_ms, enemy_list_2, index=index, player_rect=player_1 )
            enemy_2.draw(screen)

            enemy_2.objetos_lanzados.update()
            enemy_2.objetos_lanzados.draw(screen)
            

        for acid in trampas_list:
            acid.draw(screen)


        for obj in estrella:
            obj.update(delta_ms)
            rotated_image = pygame.transform.rotate(obj.image, obj.angle)
            rotated_rect = rotated_image.get_rect(center=obj.rect.center)
            screen.blit(rotated_image, rotated_rect)
        
        for i in poder:
            i.update(delta_ms)
            rotated_image = pygame.transform.rotate(i.image, i.angle)
            rotated_rect = rotated_image.get_rect(center=i.rect.center)
            screen.blit(rotated_image, rotated_rect)
        
        if player_1.lives > 0:
            if score_timer >= 2000: 
                player_1.score += 2
                score_timer = 0 

        for plataforma_1 in plataforma_movil_lista:
            plataforma_1.update(400, 800, 0, 0)
            plataforma_1.draw(screen)
        
        for plataforma_2 in plataforma_movil_lista_2:
            plataforma_2.update(645, 1050, 0, 0)
            plataforma_2.draw(screen)

        for plataforma_3 in plataforma_movil_lista_3:
            plataforma_3.update(150, 595, 0, 0)
            plataforma_3.draw(screen)

        for plataforma_4 in plataforma_movil_lista_4:
            plataforma_4.update(0, 0, 120, 450)
            plataforma_4.draw(screen)

        
        #Logica del game Over
        if player_1.game_over and player_1.is_death_animation_finished==True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        player_1 = Player(x=0, y=300, speed_walk=12, speed_run=24, gravity=10, jump_power=30, frame_rate_ms=100, move_rate_ms=50, jump_height=100, p_scale=0.2, interval_time_jump=300, estrella=estrella, poderes=poder, trampas=trampa, enemigos=enemigos, enemigo_2=enemigo2)
                        enemy_list=[]
                        enemy_list.append(Enemy(x=300, y=330, speed_walk=6, speed_run=8, gravity=4, frame_rate_ms=50, move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
                        enemy_list.append(Enemy(x=1100, y=330, speed_walk=6, speed_run=8, gravity=4, frame_rate_ms=50, move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
                        enemigos.add(enemy_list)

                        enemy_2=Enemy_2(x=900, y=175, p_scale=1)
                        enemigo2.add(enemy_2)

                        reset_objects()

        if player_1.invulnerable:
            current_time = pygame.time.get_ticks()
            if current_time - player_1.invulnerable_timer >= player_1.invulnerable_duration:
                player_1.invulnerable = False  # Finalizar la invulnerabilidad si ha pasado el tiempo

        #Dibujo en pantalla de actualizaciones de personaje, plataforma, etc
        player_1.events(delta_ms, keys)
        player_1.update(delta_ms, plataform_list, player_1, index, enemy_list, plataforma_movil_lista)
        player_1.draw(screen)
        
        player_1.objetos_lanzados.update()
        player_1.objetos_lanzados.draw(screen)
        

        #Texto en pantalla de vida, puntaje y estrellas recogidas
        font=pygame.font.SysFont("arial", 20, True)

        font_score=pygame.font.SysFont("comicsans", 20, True)
        score_text = font_score.render("Score: " + str(player_1.score), True, (255, 255, 255))
        screen.blit(score_text, (600, 5))

        lives_text = font.render("Lives:", True, (255, 255, 255))
        screen.blit(lives_text, (10, 5))

        stars_text = font.render("Stars:", True, (255, 255, 255))
        screen.blit(stars_text, (300, 5))

        if player_1.pause:
            marco = pygame.image.load("images/gui/jungle/level_select/table2.png")
            marco = pygame.transform.scale(marco, (600, 500))  # Ajusta el tamaño de la imagen según sea necesario
            marco_rect = marco.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))

            pause_image=pygame.image.load("images/gui/set_gui_01/Comic/Buttons/Pause-Button.png")
            pause_image=pygame.transform.scale(pause_image, (300, 100))  # Ajusta el tamaño de la imagen según sea necesario
            pause_rect=pygame.Rect((ANCHO_VENTANA //2 -150, ALTO_VENTANA //2 -190, 90, 90))

            marco_1_image = pygame.image.load("images/gui/set_gui_01/Comic/Buttons/repeat.png")
            marco_1_image = pygame.transform.scale(marco_1_image, (100, 100))
            marco_1_rect = pygame.Rect(ANCHO_VENTANA //2 - 40, ALTO_VENTANA //2, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

            marco_2_image = pygame.image.load("images/gui/set_gui_01/Comic/Buttons/home.png")
            marco_2_image = pygame.transform.scale(marco_2_image, (100, 100))
            marco_2_rect = pygame.Rect(ANCHO_VENTANA //2 -250, ALTO_VENTANA //2, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

            marco_3_image = pygame.image.load("images/gui/set_gui_01/Comic/Buttons/reanudar.png")
            marco_3_image = pygame.transform.scale(marco_3_image, (100, 100))
            marco_3_rect = pygame.Rect(ANCHO_VENTANA //2 +150, ALTO_VENTANA //2, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario


            screen.blit(marco, marco_rect)
            screen.blit(pause_image, pause_rect)
            screen.blit(marco_1_image, marco_1_rect)
            screen.blit(marco_2_image, marco_2_rect)
            screen.blit(marco_3_image, marco_3_rect)
        
        
        if player_1.win:
            marco_win = pygame.image.load("images/gui/jungle/level_select/table2.png")
            marco_win = pygame.transform.scale(marco, (600, 500))  # Ajusta el tamaño de la imagen según sea necesario
            marco_rect_win = marco.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))

            marco_1_image_win = pygame.image.load("images/gui/jungle/pause/bg.png")
            marco_1_image_win = pygame.transform.scale(marco_1_image_win, (100, 100))
            marco_1_rect_win = pygame.Rect(510, 300, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

            marco_2_image_win = pygame.image.load("images/gui/jungle/pause/bg.png")
            marco_2_image_win = pygame.transform.scale(marco_2_image_win, (100, 100))
            marco_2_rect_win = pygame.Rect(690, 300, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

            marco_3_image_win = pygame.image.load("images/gui/jungle/pause/bg.png")
            marco_3_image_win = pygame.transform.scale(marco_3_image_win, (100, 100))
            marco_3_rect_win = pygame.Rect(870, 300, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

            nivel_1_numero_win = pygame.image.load("images/gui/jungle/bubble/1.png")
            nivel_2_numero_win = pygame.image.load("images/gui/jungle/bubble/2.png")
            nivel_3_numero_win = pygame.image.load("images/gui/jungle/bubble/3.png")

            # Ajustar el tamaño de las imágenes según sea necesario
            nivel_1_numero_win = pygame.transform.scale(nivel_1_numero_win, (35, 70))
            nivel_1_rect_win = pygame.Rect(540, 315, 90, 90)
            nivel_2_numero_win = pygame.transform.scale(nivel_2_numero_win, (70, 70))
            nivel_2_rect_win = pygame.Rect(705, 315, 90, 90)
            nivel_3_numero_win = pygame.transform.scale(nivel_3_numero_win, (70, 70))
            nivel_3_rect_win = pygame.Rect(885, 315, 90, 90)

            screen.blit(marco_win, marco_rect_win)
            screen.blit(marco_1_image_win, marco_1_rect_win)
            screen.blit(marco_2_image_win, marco_2_rect_win)
            screen.blit(marco_3_image_win, marco_3_rect_win)
            screen.blit(nivel_1_numero_win, nivel_1_rect_win)
            screen.blit(nivel_2_numero_win, nivel_2_rect_win)
            screen.blit(nivel_3_numero_win, nivel_3_rect_win)

        pygame.display.flip()
