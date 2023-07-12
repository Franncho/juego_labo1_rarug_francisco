import pygame
from constantes import *
from pygame.locals import *
import sys

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), 16)
timer = pygame.time.Clock()

def historia():
    from main import main
    
    pygame.font.init()
    font_prueba = pygame.font.Font("freesansbold.ttf", 24)

    mensajes = ['Apriete enter para ver la historia',
                'Chano era un robot en busca de tres estrellas.',
                'En su camino, debía superar desafíos y obstáculos en distintos niveles.',
                'Se embarcó en una misión para recolectar tres valiosas estrellas.',
                'El mundo que exploraba estaba lleno de desafíos y peligros...',
                'En su búsqueda, se enfrentó a enigmáticos laberintos, desiertos desolados y cuevas oscuras.',
                'Con determinación, Chano superó cada obstáculo y logró adquirir las tres estrellas necesarias.',
                'Ahora, estaba listo para enfrentar un nuevo y emocionante desafío',
                'que lo llevaría más allá de los límites conocidos...',
                'Pulsa "Menu" para ir a la pantalla principal']

    fondo = pygame.image.load("images/gui/set_gui_01/Comic/menu/espacio.jpg").convert() # Ruta a tu imagen de fondo
    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    counter = 0
    done = False
    speed = 3
    active_message = 0
    mensaje = mensajes[active_message]

    run = True

    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(fondo, (0, 0))

        if counter < speed * len(mensaje):
            counter += 1
        elif counter >= speed * len(mensaje):
            done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done:
                    active_message += 1
                    if active_message >= len(mensajes):
                        active_message = 0
                    done = False
                    mensaje = mensajes[active_message]
                    counter = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if marco_menu_rect.collidepoint(event.pos):
                        main()


        snip = font_prueba.render(mensaje[0:counter // speed], True, C_WHITE)
        text_rect = snip.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))
        pygame.draw.rect(screen, (0, 0, 0, 100), text_rect)
        screen.blit(snip, text_rect)

        marco_menu_image = pygame.image.load("images/gui/set_gui_01/Large Buttons/Menu Button.png")
        marco_menu_image = pygame.transform.scale(marco_menu_image, (300, 100))
        marco_menu_rect = pygame.Rect(ANCHO_VENTANA //2 -130, ALTO_VENTANA //2 +100, 290, 90) 
        
        screen.blit(marco_menu_image, marco_menu_rect)

        pygame.display.update()

    pygame.quit()
    sys.exit()