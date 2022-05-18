"""
Realizar un programa que permita buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].
"""
import random

a = 0
may = 0

while a < 10000:
    num = random.randint(0, 100000)
    if num > may:
        may = num
    a += 1

print(f'El mayor de los 10000 números es: {may}')
