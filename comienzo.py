import pygame
from constantes import *
from pygame.locals import *
import sys

screen= pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), 16)
timer = pygame.time.Clock()

def comienzo():
    font_prueba=pygame.font.Font("freesansbold.ttf", 24)
    
    mensajes=['Estoy probando',
            'hola',
            'empeza a jugar']

    snip=font_prueba.render("", True, C_WHITE)
    counter=0
    done=False
    speed=3
    active_message=0
    mensaje=mensajes[active_message]

    run =True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(C_RED)
        timer.tick(60)
        pygame.draw.rect(screen, C_BLACK, [0, 300, 800, 200])

        if counter <speed *len(mensaje):
            counter+=1
        elif counter >= speed * len(mensaje):
            done=True

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN and done and active_message <len(mensajes):
                active_message +=1
                done=False
                mensaje=mensajes[active_message]
                counter=0
        
        snip=font_prueba.render(mensaje[0:counter//speed], True, C_WHITE)
        screen.blit(snip, (10, 310))
