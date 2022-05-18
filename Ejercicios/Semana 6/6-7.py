"""
Se pide desarrollar un programa que permita leer una serie de números. La finalización de carga de datos se presenta
cuando el usuario ingrese un número negativo.

Los requerimientos funcionales del programa son:

a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.

b) Cantidad de valores pares ingresados.

c) Cantidad de valores impares ingresados.

d) Informar si en la carga de números se ingresó al menos un número 0.

e) Informar si la serie contiene solo números pares e impares alternados
"""

pares = impares = suma = 0
cero = False
alternados = True

num = int(input('Ingrese el primer numero de la serie: '))

while num >= 0:

    if num == 0:
        cero = True

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if 50 <= num <= 100:
        suma += num

    anterior = num
    num = int(input('Ingrese el siguiente numero de la serie: '))

    if num % 2 == anterior % 2:
        alternados = False

print(f'La sumatoria de los valores comprendidos en el intervalo [50, 100] fue: {suma}.')
print(f'Se ingresaron un total de {pares} números pares y {impares} impares.')

if cero:
    print('Se ingreso al menos un número cero en la serie.')
else:
    print('No se ingreso ningún número cero en la serie.')

if alternados:
    print('En esta serie solo se ingresaron números pares e impares alternados.')
else:
    print('En esta serie no se ingresaron números pares e impares alternados constantemente.')
