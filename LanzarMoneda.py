import random
print('Lanzaré una mineda 199 veces. Adivina cuantas veces caerá Cara. (Presiona enter para comenzar)')
input()
lanzamientos = 0
caras = 0
while lanzamientos < 1000:
    if random.randint(0, 1)==1:
        caras = caras + 1
    lanzamientos = lanzamientos + 1

    if lanzamientos == 900:
        print('900 lanzamientos y hubo ' + str(caras) + 'caras.')
