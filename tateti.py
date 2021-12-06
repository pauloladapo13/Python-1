# Ta Te Ti

import random 

def dibujarTablero(tablero):
    # Esta función dibuja el tablero recibido como argumento.
    
    # "tablero" es una ista de 10 cadenas representando la pizarra(ignora índice 0)
    print('   |   |')
    print(' ' + tablero[7] + ' | ' + tablero[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[1] + ' | ' + tablero[3])
    print('   |   |')

def ingresaLetraJugador():
    # Permite al jugador typear que letra desea ser.
    # Devuelve una lista con las letras de los jugadores como primer item, y la letra de la computadora.
    letra = ''
    while not (letra =='X' or letra == '0'):
        print('¿Deseas ser X o 0?')
        letra = input().upper()
        
        # el primer elemento de la lista es la letra del jugador, el segundo es la letra de la computadora.
    if letra == 'X':
        return ['x', '0']
    else:
        return ['0', 'X']

def quienComienza():
    # Elije al azar que jugador comienza.
    if random.randint(0, 1) == 0:
        return 'La computadora'
    else:
        return 'El jugador'

def jugarDeNuevo():
    # Esta función devuelve  True si el jugador desea volver a jugar, de lo contrario devuelve False (Falso).
    print('¿Deseas volver a jugar? (sí/no)?')
    return input().lower().startswith('s')

def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra

def esGanador(ta, le):
    # Dado un tablero y la letra de un jugador, devuelve True (verdadero) si el mismo ha ganado
    # Utilizamos reeplazamos tablero por ta y letra por le para no escribir tanto.
    return ((ta[7] == le and ta[8] == le and ta[9] == le) or # horizontal superior
    (ta[4] == le and ta[5] == le and ta[6] == le) or # horizontal medio
    (ta[1] == le and ta[2] == le and ta[3] == le) or # horizontal inferior
    (ta[7] == le and ta[4] == le and ta[1] == le) or # vertical izquierda
    (ta[8] == le and ta[5] == le and ta[2] == le) or # vertical medio
    (ta[9] == le and ta[6] == le and ta[3] == le) or # vertical derecha
    (ta[7] == le and ta[5] == le and ta[3] == le) or # diagonal
    (ta[9] == le and ta[5] == le and ta[1] == le)) # diagonal

def obtenerDuplicadoTablero(tablero):
# Duplica la lista del tablero y devuelve el duplicado.
    dupTablero = []

    for i in tablero:
        dupTablero.append(i)
    
    return dupTablero

def hayEspacioLibre(tablero, jugada):
    # Devuelve true si hay espacio para efectuar la jugada en el tablero.
    return tablero[jugada] == ' '

def obtenerJugadaJugador(tablero):
    # Permite al jugador escribir su ugada.
    jugada = ' ' 
    while jugada not in '1 2 3 4 5 6 7 8 9 '.split() or not hayEspacioLibre(tablero, int(jugada)):
        print('¿Cuál es tu próxima jugada? (1-9)')
        jugada = input()
    return int(jugada)

def elegirAzarDeLista(tablero, listaJugada):
    # Devuelve una jugada válida en el tablero de la lista recibida.
    # Devuelve None si no hay minguna jugada válida.
    jugadasPosibles = []
    for i in listaJugada:
        if hayEspacioLibre(tablero, i):
            jugadasPosibles.append(i)
    
    if len(jugadasPosibles) != 0:
            return random.choice(jugadasPosibles)
    else:
            return None

def obtenerJugadaComputadora(tablero, letraComputadora):
    # Dado un tablero y la letra de la computadora, determina que jugada efectuar.
    if letraComputadora == 'X':
        letraJugador = '0'
    else:
        letraJugador = 'X'
    
    # Aquí está nuestro algoritmo para nuestra IA ( Inteligencia Artificial) del Ta Te Ti.
    # Primero, verifica si podemos ganar en la próxima jugada
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraComputadora, i)
            if esGanador(copia, letraComputadora):
                return i 
            
    # Verifica si el jugador podría ganar en su próxima jugada, y lo bloquea.
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraJugador, i)
            if esGanador(copia, letraJugador):
                return i 
    
    # Intenta ocupar una de las esquinas de estar libre.
    jugada = elegirAzarDeLista(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada 
    
    # De estar libre, intenta ocupar el centro.
    if hayEspacioLibre(tablero, 5):
        return 5
    
    # Ocupa alguno de los lados.
    return elegirAzarDeLista(tablero, [2, 4, 6, 8])

def tableroCompleto(tablero):
    # Devuelve True si cada espcio de tablero fue ocupado, caso contrario devuelve False.
    for i in range(1, 10):
        if hayEspacioLibre(tablero, i):
            return False
    return True


print('¡Bienvenido al Ta Te Ti!')

while True:
    # Resetea el tablero
    elTablero = [' '] * 10
    letraJugador, letraComputadora = ingresaLetraJugador()
    turno = quienComienza()
    print(turno + ' irá primero.')
    juegoEnCurso = True
    
    while juegoEnCurso:
        if turno == 'El jugador':
            #Turno del jugador
            dibujarTablero(elTablero)
            jugada = obtenerJugadaJugador(elTablero)
            hacerJugada(elTablero, letraJugador, jugada)
            
            if esGanador(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('¡Felicidades, has ganado!')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Es un empate!')
                    break
                else:
                    turno = 'La computadora'
        else:
            # Turno de la computadora
            jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
            hacerJugada(elTablero, letraComputadora, jugada)
            
            if esGanador(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('¡La computadora te ha vencido! Has perdido.')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('¿Es un empate!')
                    break
                else:
                    turno ='El jugador'
                    
    if not jugarDeNuevo(): 
            break

