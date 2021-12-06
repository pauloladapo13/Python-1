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
  ============''']
palabras =''' go_back come_back ask_for put_on take_off 
get_back take_back give_up bring_up come_up find_out figure_out
hurry_up make_up show_up turn_on turn_off get_along think_about
think_of break_down make_up come_up_with cath_up throw_up wind_up
end_up cheer_up get_up wake_up grow_up mix_up pick_up put_up stand_up_to 
stand_somebody_up stand_up_for stay_up work_up think_up look_up_to turn_up 
break_up back_out chicken_out come_out cut_out drop_out duck_out fall_out 
fill_out find_out figure_out get_out_of give_out go_out hang_out head_out 
hear_our help_out kick_out point_out put_out'''.split()
def obtenerPalabraAlAzar(listaDePalabras):
    #Esta función devuelve una cadena al azar de la lista de cadenas psada como argumento.
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]

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
palabraSecreta = obtenerPalabraAlAzar(palabras)
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
            print('¡Sí! ¡La palabra  secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            juegoTerminado = True
            break
            
            
    else: 
        letrasIncorrectas = letrasIncorrectas + intento
        # Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
            mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
            
            juegoTerminado = True 
            
        # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
        if juegoTerminado:
            if jugarDeNuevo():
                letrasIncorrectas = ''
                letrasCorrectas = ''
                juegoTerminado = False 
                palabraSecreta = obtenerPalabraAlAzar(palabras)
            else: 
                break 
            