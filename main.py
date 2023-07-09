import pygame
from constantes import *
from nivel_1 import *


pygame.init()

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Ingrese Nivel")

fondo = pygame.image.load("images/gui/jungle/menu/bg.png").convert()
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

marco = pygame.image.load("images/gui/jungle/level_select/table2.png")
marco = pygame.transform.scale(marco, (600, 500))  # Ajusta el tamaño de la imagen según sea necesario
marco_rect = marco.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))

marco_1_image = pygame.image.load("images/gui/jungle/pause/bg.png")
marco_1_image = pygame.transform.scale(marco_1_image, (100, 100))
marco_1_rect = pygame.Rect(510, 300, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

marco_2_image = pygame.image.load("images/gui/jungle/pause/bg.png")
marco_2_image = pygame.transform.scale(marco_2_image, (100, 100))
marco_2_rect = pygame.Rect(690, 300, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

marco_3_image = pygame.image.load("images/gui/jungle/pause/bg.png")
marco_3_image = pygame.transform.scale(marco_3_image, (100, 100))
marco_3_rect = pygame.Rect(870, 300, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

nivel_1_numero = pygame.image.load("images/gui/jungle/bubble/1.png")
nivel_2_numero = pygame.image.load("images/gui/jungle/bubble/2.png")
nivel_3_numero = pygame.image.load("images/gui/jungle/bubble/3.png")

# Ajustar el tamaño de las imágenes según sea necesario
nivel_1_numero = pygame.transform.scale(nivel_1_numero, (35, 70))
nivel_1_rect = pygame.Rect(540, 315, 90, 90)
nivel_2_numero = pygame.transform.scale(nivel_2_numero, (70, 70))
nivel_2_rect = pygame.Rect(705, 315, 90, 90)
nivel_3_numero = pygame.transform.scale(nivel_3_numero, (70, 70))
nivel_3_rect = pygame.Rect(885, 315, 90, 90)

def main():
    # Lógica del juego

    from nivel_2 import nivel_2
    
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

        if current_level == 1:
            nivel_1()
        elif current_level == 2:
            nivel_2()
        elif current_level == 3:
            pass
        # Añade más niveles según sea necesario

        screen.blit(fondo, (0, 0))
        screen.blit(marco, marco_rect)
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
