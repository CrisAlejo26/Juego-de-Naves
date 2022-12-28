import pygame

pygame.init()

# Vamos a ver la pantalla y ponemos alto y ancho en una tupla
pantalla = pygame.display.set_mode((800, 600))

seEjecuta = True

while seEjecuta:
    # Realiza un recorrido validando los eventos en la ventanda
    for evento in pygame.event.get():
        # Si encuentra un evento de salir entonces:
        if evento.type == pygame.QUIT:
            seEjecuta = False