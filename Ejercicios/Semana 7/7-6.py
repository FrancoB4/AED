"""
Desarrollar un programa que permita ingresar las coordenadas de n puntos en el plano, e informe:

a) En qué cuadrante se encuentra cada uno.

b) Determinar cuántos puntos se encuentran en el primer o tercer cuadrante.

c) Determinar cuál de todos los puntos cargados se encuentra a mayor distancia del origen de coordenadas.
"""

cuadrantes_1_3 = 0
mayor = None
x_may = 0
y_may = 0

n = int(input('Ingrese n: '))

for i in range(1, n + 1):
    x = int(input('Ingrese x: '))
    y = int(input('Ingrese y: '))
    dist = round(pow(pow(x, 2) + pow(y, 2), .5), 2)

    if mayor is None or dist > mayor:
        x_may = x
        y_may = y
        mayor = dist

    if x < 0:
        if y < 0:
            print(f'El punto {(x, y)} se encuentra en el cuadrante 3.')
            cuadrantes_1_3 += 1
        else:
            print(f'El punto {(x, y)} se encuentra en el cuadrante 2.')
    else:
        if y < 0:
            print(f'El punto {(x, y)} se encuentra en el cuadrante 4.')
        else:
            print(f'El punto {(x, y)} se encuentra en el cuadrante 1.')
            cuadrantes_1_3 += 1

print(f'En el primer y tercer cuadrante hay un total de {cuadrantes_1_3} puntos.')
print(f'El punto mas lejano del origen es el punto {(x_may, y_may)} que se encuentra a una '
      f'distancia de {mayor} unidades.')
