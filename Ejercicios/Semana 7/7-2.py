"""
Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:

a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.

b) Determinar en qué mes recibió el sueldo más bajo del período.

c) Informar el sueldo promedio del semestre.
"""
num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro: '))

if num1 < num2:
    men, may = num1, num2
else:
    men, may = num2, num1

if men % 2 == 0:
    men += 1
if may % 2 == 0:
    may -= 1

print('Secuencia ascendente:')
ascend = range(men, may + 1, 2)
for num in ascend:
    print(num, end=' | ')

print('\nSecuencia descendente:')
descend = range(may, men -1, -2)
for num in descend:
    print(num, end=' | ')