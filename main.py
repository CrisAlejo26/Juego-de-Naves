import pygame
import random
import math

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
enemigoMalvado = []
# Cargo las coordenadas maximas para el enemigo
enemigoX = []
enemigoY = []
# Se devuelve cuando toca los bordes
enemigo_x_cambio = []
# Lo que va a ir bajando
enemigo_y_cambio = []
cantidadEnemigos = 8

for e in range(cantidadEnemigos):
    # Cargo la imagen
    enemigoMalvado.append(pygame.image.load("enemigo.png"))
    # Cargo las coordenadas maximas para el enemigo
    enemigoX.append(random.randint(0, 736))
    enemigoY.append(random.randint(50, 200))
    # Se devuelve cuando toca los bordes
    enemigo_x_cambio.append(2)
    # Lo que va a ir bajando
    enemigo_y_cambio.append(50)

# ! Bala
# Cargo la imagen
imgBala = pygame.image.load("bala.png")
# Cargo las coordenadas maximas para la bala
balaX = 0
balaY = 500
# Se devuelve cuando toca los bordes
bala_x_cambio = 0
# Velocidad de la bala
bala_y_cambio = 3
balaVisible = False

# ! Puntaje
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
textoX = 10
textY = 10

# ! Funcion mostrar Puntaje
def mostrarPuntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

# ! Funcion Jugador
def jugador(x, y):
    # Colocamos el personaje principal en pantalla
    pantalla.blit(jugadorPrincipal, (x, y))
    
# ! Funcion Enemigo
def enemigo(x, y, g):
    # Colocamos el enemigo en pantalla
    pantalla.blit(enemigoMalvado[g], (x, y))

# ! Funcion disparar bala
def dispararBala(x, y):
    # la bala debe ser visible
    global balaVisible
    balaVisible = True
    # Esto se hace para que la bala salga desde la mitad de la nave
    pantalla.blit(imgBala, (x + 16, y + 10))

# ! Funcion detectar colisiones

def colisiones(x1, y1, x2, y2):
    # Raiz cuaddrada y dentro un exponente
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y2 - y1, 2))
    if distancia < 27:
        return True
    else:
        return False

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
                jugador_x_cambio = -2
            # Si presiona la tecla flecha izquierda
            if evento.key == pygame.K_RIGHT:
                # La nave se mueve a la derecha cuando presione la flecha
                jugador_x_cambio = 2
            if evento.key == pygame.K_SPACE:
                if not balaVisible:
                    balaX = jugadorX
                    dispararBala(balaX, balaY)
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
    for e in range(cantidadEnemigos):
        enemigoX[e] += enemigo_x_cambio[e]
        
        # ! Mantener dentro de los bordes al enemigo
        # Si el enemigo llega a posicion 0, entonces se devuelve
        if enemigoX[e] <= 0:
            enemigo_x_cambio[e] = 2
            # Baja el valor que tiene enemigo_y_cambio
            enemigoY[e] += enemigo_y_cambio[e] 
        # Si el enemigo llega a posicion 736, entonces se devuelve
        elif enemigoX[e] >= 736:
            enemigo_x_cambio[e] = -2
            # Baja el valor que tiene enemigo_y_cambio
            enemigoY[e] += enemigo_y_cambio[e] 
            
        # ! Colision
        coli = colisiones(enemigoX[e], enemigoY[e], balaX, balaY)
        if coli:
            balaY = 500
            balaVisible = False
            puntaje += 1
            enemigoX[e] = random.randint(0, 736)
            enemigoY[e] = random.randint(50, 200)
        
        enemigo(enemigoX[e], enemigoY[e], e)
    
    # ! Movimiento bala
    if balaY <= -64:
        balaY = 500
        balaVisible = False
    if balaVisible:
        dispararBala(balaX, balaY)
        balaY -= bala_y_cambio
    
    jugador(jugadorX, jugadorY)
    mostrarPuntaje(textoX, textY)
    
    # ! Actualizar siempre al final del ciclo
    pygame.display.update()

