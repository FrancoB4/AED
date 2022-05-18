"""
Desarrollar un programa que, ingresando los dos catetos de un triángulo rectángulo, informe:

Valor de la hipotenusa (redondeado a 2 decimales)
Valor del lado mayor
Valor del lado menor
"""
c1 = float(input('Cateto 1: '))
c2 = float(input('Cateto 2: '))

hypotenuse = round(pow((c2**2 + c1**2), 1/2), 2)
minor_side = min(c1, c2)
major_side = max(c1, c2)

print(f'La s medidas del triangulo son: \n  Hipotenusa: {hypotenuse}\n  Lado menor: {minor_side}\n  '
      f'Lado mayor: {major_side}')
