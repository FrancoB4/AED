"""
Realizar un programa que genere 5000 números aleatorios en el rango de [0, 100000] y que permita:

Determinar el menor de los números generados en forma aleatoria
Calcular el valor promedio de los números menores a 10.000.
"""
import random

a = 0
men = 100000
suma = cont = 0

while a < 5000:
    num = random.randint(0, 100000)
    if num < men:
        men = num
    if num < 10000:
        cont += 1
        suma += num

    a += 1

print(f'El menor de los números fue {men}')
print(f'El valor promedio de los números menores a 10000 fue: {suma/cont}')
