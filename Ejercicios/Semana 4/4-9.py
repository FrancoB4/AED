"""
Ingresar por teclado las edades de 3 participantes de un concurso.

Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por teclado.
"""

e1 = int(input('Edad 1: '))
e2 = int(input('Edad 2: '))
e3 = int(input('Edad 3: '))
e_minima = int(input('Edad minima: '))

if e1 > e_minima and e2 > e_minima and e3 > e_minima:
    print('Todos cumplen con la edad minima.')
else:
    print('Algunos de las edades ingresadas no satisface la edad minima ingresada.')
