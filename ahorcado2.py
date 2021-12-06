import random
IMÁGENES_AHORCADO = ['''
                                          
      +---+
      |   |
          |
          |
          |
          |
  ============''', '''
  
      +---+
      |   |
      O   |
          |
          |
          |
  ============''', '''

      +---+
      |   |
      O   |
      |   |
          |
          |
  ============''', '''

      +---+
      |   |
      O   |
     /|   |
          |
          |
  ============''', '''

      +---+
      |   |
      O   |
     /|\  |
          |
          |
  ============''', '''

      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
  ============''', '''

      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
  ============''', '''

      +---+
      |   |
     [O   |
     /|\  |
     / \  |
          |
  ============''', '''

      +---+
      |   |
     [O]  |
     /|\  |
     / \  |
          |
  ============''']
palabras ={'volver': 'go_back', 'volver' : 'come_back', 'pedir' : 'ask_for', 'ponerse':'put_on', 'quitarse':'take_off', 
'volver (sitio de residencia habitual)' : 'get_back', 'devolver' : 'take_back', 'abandonar':'give_up', 'sacar un tema':'bring_up', 'acercarse':'come_up', 'enterarse, averiguar':'find_out', 'entender, descifrar':'figure_out',
'Darse prisa':'hurry_up', 'inventarse, compensar':'make_up', 'aparecer':'show_up', 'encender':'turn_on', 'apagar':'turn_off', 'llevarse bien con alguien':'get_along', 'pensar reflexivamente':'think_about',
'pensar escogiendo':'think_of', 'averiar, desglosar':'break_down', 'inventar, compensar, hacer las paces':'make_up', 'dar con algo':'come_up_with', 'alcanzar':'cath_up', 'vomitar':'throw_up', 'Terminar por':'wind_up', 
'terminar por': 'end_up', 'animarse, animar':'cheer_up', 'levantarse':'get_up', 'despertarse':'wake_up', 'madurar':'grow_up', 'confundirse':'mix_up', 'recoger':'pick_up', 'soportar':'put_up', 'plantar cara a alguien':'stand_up_to_sb', 
'dar plantón a alguien':'stand_somebody_up', 'defender a alguien':'stand_up_for', 'quedarse hasta las tantas':'stay_up', 'enfadarse, contrariarse':'work_up', 'discurrir, dar con algo pensado':'think_up', 'admirar a alguien':'look_up_to', 'subir el volumen':'turn_up', 
'dejarlo con alguien, dividir':'break_up', 'retirarse, desvincularse':'back_out', 'acobardarse':'chicken_out', 'salir de detrás de algo, salir(libro, album)':'come_out', 'cortar el rollo':'cut_out', 'abandonar(escuela, etc)':'drop_out', 'escaquearse':'duck_out', 'enfadarse':'fall_out', 
'rellenar ficha, etc':'fill_out', 'enterarse, averiguar':'find_out', 'descifrar':'figure_out', 'salir de sitio pequeño y dificultoso':'get_out_of', 'repartir':'give_out', 'salir':'go_out', 'pasar el rato con alguien':'hang_out', 'marcharse, emprender viaje':'head_out', 
'oír lo que te tienen que decir':'hear_out', 'echar una mano':'help_out', 'expulsar':'kick_out', 'puntualizar':'point_out', 'apagar fuego':'put_out'}
def obtenerPalabraAlAzar(listaDePalabras):
    #Esta función devuelve una cadena al azar de la lista de cadenas psada como argumento.
    # Primero, elige una clave al azar del diccionario:
    claveDePalabras = random.choice(list(palabras.keys()))
    # Segundo, elige una palabra aleatoria de la lista correpondiente a la clave en el diccionario:
    indiceDePalabras = random.randint(0, len(listaDePalabras[claveDePalabras]) - 1)
    return [listaDePalabras[claveDePalabras], claveDePalabras]

def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    print()
    
    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print() 
    
    espaciosVacios = '_' * len(palabraSecreta)
    
    for i in range(len(palabraSecreta)): 
    # completar los espacios vacios las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]
    for letra in espaciosVacios: 
        #mostrar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()
    
def obtenerIntento(letrasProbadas):
    #Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
    while True:
        print('Adivina una letra:')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz_':
            print('Por favor ingresa una LETRA')
        else:
            return intento
def jugarDeNuevo():
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('¿Quieres jugar de nuevo? (si o no)')
    return input().lower().startswith('s')

print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta, claveSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
    #permite al jugador escribir una letra.
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
        # Verifica si el jugador ha ganado.
        encontradoTodasLasLetras = True 
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False 
                break 
        if encontradoTodasLasLetras:
            print('¡Sí! ¡La palabra  secreta es "' + palabraSecreta + '"! ¡Has ganado!'' y en español significa ' + claveSecreta )
            juegoTerminado = True
            
            
            
            
    else: 
        letrasIncorrectas = letrasIncorrectas + intento
        # Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
            mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"' ' y la palabra en español es ' + claveSecreta)
            
            juegoTerminado = True 
            
        # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
        if juegoTerminado:
            if jugarDeNuevo():
                letrasIncorrectas = ''
                letrasCorrectas = ''
                juegoTerminado = False 
                palabraSecreta, claveSecreta = obtenerPalabraAlAzar(palabras)
            else: 
                print(' El juego ha terminado.')
                break 
            