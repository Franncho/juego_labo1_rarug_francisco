import pygame
from constantes import *

pygame.init()

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Ingrese Nivel")

fondo = pygame.image.load("images/gui/set_gui_01/Comic/menu/espacio.jpg").convert()
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

text_level_image=pygame.image.load("images/gui/set_gui_01/Large Buttons/Start_BTN.png")
text_level_image = pygame.transform.scale(text_level_image, (300, 100))
text_level_rect = pygame.Rect(ANCHO_VENTANA //2 -150, ALTO_VENTANA //2 -190, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

marco_1_image = pygame.image.load("images/gui/set_gui_01/Large Buttons/Window.png")
marco_1_image = pygame.transform.scale(marco_1_image, (100, 100))
marco_1_rect = pygame.Rect(ANCHO_VENTANA //2 - 40, ALTO_VENTANA //2, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

historia_image = pygame.image.load("images/gui/set_gui_01/Large Buttons/Window.png")
historia_image = pygame.transform.scale(historia_image, (100, 100))
historia_rect = pygame.Rect(ANCHO_VENTANA //2-40, ALTO_VENTANA //2 +200, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

marco_2_image = pygame.image.load("images/gui/set_gui_01/Large Buttons/Window.png")
marco_2_image = pygame.transform.scale(marco_2_image, (100, 100))
marco_2_rect = pygame.Rect(ANCHO_VENTANA //2 -250, ALTO_VENTANA //2, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

marco_3_image = pygame.image.load("images/gui/set_gui_01/Large Buttons/Window.png")
marco_3_image = pygame.transform.scale(marco_3_image, (100, 100))
marco_3_rect = pygame.Rect(ANCHO_VENTANA //2 +150, ALTO_VENTANA //2, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

nivel_1_numero = pygame.image.load("images/gui/set_gui_01/Comic_Border/Buttons/1.png")
nivel_2_numero = pygame.image.load("images/gui/set_gui_01/Comic_Border/Buttons/2.png")
nivel_3_numero = pygame.image.load("images/gui/set_gui_01/Comic_Border/Buttons/3.png")

historia_logo = pygame.image.load("images/gui/set_gui_01/Comic/Buttons/logo_libro.png")

# Ajustar el tamaño de las imágenes según sea necesario
nivel_1_numero = pygame.transform.scale(nivel_1_numero, (35, 70))
nivel_1_rect = pygame.Rect(ANCHO_VENTANA //2 -210 -7, ALTO_VENTANA//2 +15 , 90, 90)
nivel_2_numero = pygame.transform.scale(nivel_2_numero, (70, 70))
nivel_2_rect = pygame.Rect(ANCHO_VENTANA // 2 -25, ALTO_VENTANA//2 +15 , 90, 90)
nivel_3_numero = pygame.transform.scale(nivel_3_numero, (70, 70))
nivel_3_rect = pygame.Rect(ANCHO_VENTANA // 2 +165, ALTO_VENTANA//2 +15 , 90, 90)

historia_logo = pygame.transform.scale(historia_logo, (70, 70))
historia_logo_rect = pygame.Rect(ANCHO_VENTANA //2 -25, ALTO_VENTANA//2 +215 , 90, 90)

def main():
    # Lógica del juego

    from nivel_1 import nivel_1
    from nivel_2 import nivel_2
    from nivel_3 import nivel_3
    from history import historia
    
    running = True
    current_level = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if nivel_1_rect.collidepoint(event.pos):
                    current_level = 1
                elif nivel_2_rect.collidepoint(event.pos):
                    current_level = 2
                elif nivel_3_rect.collidepoint(event.pos):
                    current_level = 3
                elif historia_rect.collidepoint(event.pos):
                    current_level = 4
        
        if current_level == 1:
            nivel_1()
        elif current_level == 2:
            nivel_2()
        elif current_level == 3:
            nivel_3()
        elif current_level == 4 :
            historia()
        # Añade más niveles según sea necesario

        screen.blit(fondo, (0, 0))
        screen.blit(text_level_image, text_level_rect)
        screen.blit(historia_image, historia_rect)
        screen.blit(historia_logo, historia_logo_rect)
        screen.blit(marco_1_image, marco_1_rect) 
        screen.blit(marco_2_image, marco_2_rect)
        screen.blit(marco_3_image, marco_3_rect)
        screen.blit(nivel_1_numero, nivel_1_rect)
        screen.blit(nivel_2_numero, nivel_2_rect)
        screen.blit(nivel_3_numero, nivel_3_rect)
        pygame.display.flip()  # Actualizar la pantalla en cada iteración del bucle

    pygame.quit()

if __name__ == "__main__":
    main()
