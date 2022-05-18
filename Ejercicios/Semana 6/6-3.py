"""Realice un programa que le ofrezca al usuario un menú de opciones que le permita ejecutar las siguientes acciones:

Opción 1: Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000].

Opción 2: Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].

Opción 3: Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] y calcular el valor promedio
de los números menores a 10.000.

Cualquier otro número: Salir del programa."""
from random import randint
n = int(input('Bienvenido al menu de opciones\n'
              'Para opción 1 marque 1:\n'
              'Para opción 2 marque 2:\n'
              'Para opción 3 Marque 3:\n'))

cont = 0

if n == 1:
    a = 1000
    suma = 0
    while a > 0:
        suma += randint(0, 100000)
        cont += 1
        a -= 1
    print(f'El promedio es {suma/cont}')
elif n == 2:
    a = 10000
    men = 0

    while a > 0:
        num = randint(0, 100000)
        if a == 10000 or num < men:
            men = num

        a -= 1
    print(f'El menor de los 10000 numeros es: {men}')
elif n == 3:
    a = 5000
    may = 0
    men_5000 = 0
    sum_men = 0
    while a > 0:
        num = randint(0, 100000)
        if num < 10000:
            sum_men += num
            men_5000 += 1
        if a == 5000 or num > may:
            may = num
        a -= 1

    print(f'El mayor numero es: {may}\nEl promedio de los numeros menores a 10000 es: {sum_men/men_5000}')
else:
    a = 1000
    suma = 0
    while a > 0:
        sum += randint(0, 100000)
        cont += 1
        a -= 1
    print(f'El promedio es {suma / cont}')

cont = 0

while a > 0:
    a += randint(0, 100000)
    cont += 1

