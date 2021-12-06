# Este es el juego de adivinar el número.
import random

intentosRealizados = 0

print('¡Hola!, ¿Cómo te llamas?')

miNombre = input()

número = random.randint(1, 20)
print('¿Te crees tan listillo?XD, ' + miNombre + ' . Estoy pensando en un número entre el 1 y el 20.' +
      ' ¿Podrás adivinarlo o serás un Don Ampeter?=)')

while intentosRealizados <= 6:
    print('¿Eres lo bastante listo para entrar a infantil XD?')
    estimación = input('¡inserta número amigo!:')
    estimación = int(estimación)

    intentosRealizados = intentosRealizados + 1

    if estimación < número:
        print('Demasiado bajo, perdedor. ;)')
    if estimación > número:
        print(' Demasiado alto, genio. :l ')
    if estimación == número:
        print('¡Eso es crack, tampoco costaba tanto ehh')
        break
if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo, ' + miNombre +
          '! ¡Has adivinado el número en ' + intentosRealizados + ' intentos!')

if estimación != número:
    número = str(número)
    print('Pues no. El número que estaba pensando era ' + número)
    
    print('A ver si esta vez lo adivinas antes, te apuntas? ') 

reset