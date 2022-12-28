import pygame

# ! Inicializar Pygame
pygame.init()

# ? Crear pantalla
# Vamos a ver la pantalla y ponemos alto y ancho en una tupla
pantalla = pygame.display.set_mode((800, 600))

# ? Titulo e icono
# Titulo
pygame.display.set_caption("Invasion Espacial")
# Icono de la ventada
icono = pygame.image.load("ovni_icono.png")
# Enviamos el icono a la ventada
pygame.display.set_icon(icono)


# ! Jugador
# Cargo la imagen
jugadorPrincipal = pygame.image.load("NavePrincipal.png")
# Cargo las coordenadas
jugadorX = 368
jugadorY = 534

def jugador(x, y):
    # Colocamos el personaje principal en pantalla
    pantalla.blit(jugadorPrincipal, (x, y))


# ! Loop del juego
seEjecuta = True
while seEjecuta:
    # Relleno de pantalla
    pantalla.fill((205, 144, 227))
    
    # Realiza un recorrido validando los eventos en la ventanda
    for evento in pygame.event.get():
        # Si encuentra un evento de salir entonces:
        if evento.type == pygame.QUIT:
            seEjecuta = False
        # Si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            # Si presiona la tecla flecha izquierda
            if evento.key == pygame.K_LEFT:
                print("flecha izquierda presionada")
            # Si presiona la tecla flecha izquierda
            if evento.key == pygame.K_RIGHT:
                print("flecha derecha presionada")
        # Si el usuario suela una tecla        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                print(" La flecha fue soltada ")
    jugador(jugadorX, jugadorY)
    
    pygame.display.update()

