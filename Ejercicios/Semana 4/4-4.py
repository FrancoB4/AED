"""Se solicita realizar un programa que permita ingresar tres temperaturas correspondientes a diferentes momentos de
un día y determinar:

Cuál es el promedio de las temperaturas.
Si existe alguna temperatura que sea mayor al promedio.
"""

t1 = int(input('Temperatura 1: '))
t2 = int(input('Temperatura 2: '))
t3 = int(input('Temperatura 3: '))

average = (t1 + t2 + t3)/3
above = 0

print(f'El promedio de temperaturas es: {average}')

if t1 > average:
    above += 1
if t2 > average:
    above += 1
if t3 > average:
    above += 1

if above > 0:
    print(f'Hay {above} temperaturas por encima del promedio.')
