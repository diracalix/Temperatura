import random

# Dimensiones del laberinto
n = 5
m = 5

# Inicializar laberinto, cargamos en espacios  en blanco
laberinto = [[' ' for _ in range(m)] for _ in range(n)]

# Posiciones iniciales
raton_pos = (random.randint(0, n-1), random.randint(0, m-1))
gato_pos = (random.randint(0, n-1), random.randint(0, m-1))
salida_pos = (random.randint(0, n-1), random.randint(0, m-1))

# Asegurarse de que el ratón, el gato y la salida no están en la misma posición inicialmente
while gato_pos == raton_pos or gato_pos == salida_pos or raton_pos == salida_pos:
    raton_pos = (random.randint(0, n-1), random.randint(0, m-1))
    gato_pos = (random.randint(0, n-1), random.randint(0, m-1))
    salida_pos = (random.randint(0, n-1), random.randint(0, m-1))


def imprimir_laberinto():
    for i in range(n):
        for j in range(m):
            if (i, j) == raton_pos:
                print('R', end=' ')
            elif (i, j) == gato_pos:
                print('G', end=' ')
            elif (i, j) == salida_pos:
                print('S', end=' ')
            else:
                print('.', end=' ')
        print()
    print()


def mover_random(pos):
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    movimiento = random.choice(movimientos)
    nueva_pos = (pos[0] + movimiento[0], pos[1] + movimiento[1])

    if 0 <= nueva_pos[0] < n and 0 <= nueva_pos[1] < m:
        return nueva_pos
    else:
        return pos


# Ciclo principal del juego
while True:
    imprimir_laberinto()

    if raton_pos == gato_pos:
        print("¡El gato atrapó al ratón! El gato gana.")
        break
    elif raton_pos == salida_pos:
        print("¡El ratón encontró la salida! El ratón gana.")
        break

    # Mover ratón y gato
    raton_pos = mover_random(raton_pos)
    gato_pos = mover_random(gato_pos)
