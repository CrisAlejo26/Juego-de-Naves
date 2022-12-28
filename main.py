import pygame
import random

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
fondo = pygame.image.load("fondo.png")

# ! Jugador
# Cargo la imagen
jugadorPrincipal = pygame.image.load("NavePrincipal.png")
# Cargo las coordenadas
jugadorX = 368
jugadorY = 500
jugador_x_cambio = 0

# ! Enemigo
# Cargo la imagen
enemigoMalvado = pygame.image.load("enemigo.png")
# Cargo las coordenadas maximas para el enemigo
enemigoX = random.randint(0, 736)
enemigoY = random.randint(50, 200)
# Se devuelve cuando toca los bordes
enemigo_x_cambio = 0.3
# Lo que va a ir bajando
enemigo_y_cambio = 50

# ! Funcion Jugador
def jugador(x, y):
    # Colocamos el personaje principal en pantalla
    pantalla.blit(jugadorPrincipal, (x, y))
    
# ! Funcion Enemigo
def enemigo(x, y):
    # Colocamos el enemigo en pantalla
    pantalla.blit(enemigoMalvado, (x, y))


# ! Loop del juego
seEjecuta = True
while seEjecuta:
    # Relleno de pantalla
    pantalla.blit(fondo, (0, 0))
    
    # Realiza un recorrido validando los eventos en la ventanda
    for evento in pygame.event.get():
        # * Evento para cerrar programa
        # Si encuentra un evento de salir entonces:
        if evento.type == pygame.QUIT:
            seEjecuta = False
        # * Evento para presionar teclas
        # Si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            # Si presiona la tecla flecha izquierda
            if evento.key == pygame.K_LEFT:
                # La nave se mueve a la izquierda cuando presione la flecha
                jugador_x_cambio = -0.2
            # Si presiona la tecla flecha izquierda
            if evento.key == pygame.K_RIGHT:
                # La nave se mueve a la derecha cuando presione la flecha
                jugador_x_cambio = 0.2
        # * Evento para soltarss teclas
        # Si el usuario suela una tecla        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                # Si no se presiona nada, no se mueve la nave
                jugador_x_cambio = 0
                
    # ? Modificar ubicacion del jugador
    jugadorX += jugador_x_cambio
    
    # ! Mantener dentro de los bordes la nave
    if jugadorX <= -1:
        jugadorX = -1
    elif jugadorX >= 742:
        jugadorX = 742
    
        
    # ? Modificar la ubicacion del enemigo
    enemigoX += enemigo_x_cambio
    
    # ! Mantener dentro de los bordes al enemigo
    # Si el enemigo llega a posicion 0, entonces se devuelve
    if enemigoX <= 0:
        enemigo_x_cambio = 0.3
        # Baja el valor que tiene enemigo_y_cambio
        enemigoY += enemigo_y_cambio 
    # Si el enemigo llega a posicion 736, entonces se devuelve
    elif enemigoX >= 736:
        enemigo_x_cambio = -0.3
        # Baja el valor que tiene enemigo_y_cambio
        enemigoY += enemigo_y_cambio 
    
    jugador(jugadorX, jugadorY)
    enemigo(enemigoX, enemigoY)
    
    # ! Actualizar siempre al final del ciclo
    pygame.display.update()

