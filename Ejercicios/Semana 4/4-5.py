"""Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100, que representaría la
tarjeta de bingo de una persona. Una vez generados los números aleatorios solicitar al usuario que ingrese 3 números
enteros y a partir de alli mostrar los siguientes mensajes:

Si el usuario no marcó ninguno de los números indicarlo diciendo "El jugador tiene mala suerte, no marcó ninguna
casilla" Caso contrario mostrar "El jugador marcó algún número de la tarjeta". """
import random

numbers = [random.randint(1, 101), random.randint(1, 101), random.randint(1, 101),
           random.randint(1, 101), random.randint(1, 101), random.randint(1, 101),
           random.randint(1, 101), random.randint(1, 101), random.randint(1, 101),
           random.randint(1, 101), random.randint(1, 101), random.randint(1, 101),
           random.randint(1, 101), random.randint(1, 101), random.randint(1, 101)]

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

if n1 in numbers or n2 in numbers or n3 in numbers:
    print('El jugador marcó algún número de la tarjeta')
else:
    print('El jugador tiene mala suerte, no marcó ninguna casilla')

