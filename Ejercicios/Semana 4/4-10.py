"""
Se ingresan las medidas de frente y fondo de un terreno.

Determinar si es cuadrado o rectangular y calcular su superficie.
"""

a = float(input('Frente del terreno: '))
b = float(input('Fondo del terreno: '))

axb = round(a * b, 2)

if a == b:
    print(f'El terreno es un cuadrado de: {axb}m2 de superficie.')
else:
    print(f'El terreno es un rectángulo de : {axb}m2 de superficie.')
