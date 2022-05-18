"""
Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base, pero sabiendo
que su altura es igual al cuadrado de la base. (Observar que la altura no es un dato... solo se indica la
forma de calcularla de acuerdo a la base que sí es un dato).
"""


# Datos de Entrada:
base = float(input("Ingrese la base del triangulo: "))

# Procesos:
altura = base ** 2

# Salidas:
superficie = base * altura / 2
print(f'La superficie del triangulo es: {superficie}')
