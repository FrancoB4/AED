"""
Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:

a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.

b) Determinar en qué mes recibió el sueldo más bajo del período.

c) Informar el sueldo promedio del semestre.
"""
may = 0
men = 0
suma = 0


for i in range(1, 6 + 1):
    sueldo = float(input(f'Ingrese el sueldo para el mes {i}: '))

    if sueldo > may:
        may = sueldo

    if sueldo < men or i == 1:
        men = sueldo

    suma += sueldo

print(f'El aguinaldo correspondiente al primer semestre es de: ${round(may/2, 2)}')
print(f'El sueldo mas bajo del periodo fue de: ${men}')
print(f'El sueldo promedio de este semestre fue de: ${round(suma/6, 2)}')
