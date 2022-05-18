"""
Desarrollar un programa que permita validar la cuenta de un usuario que intenta ingresar al sistema.

La cuenta debe ingresarse con formato nombre@dominio y el programa validará que cumpla con las siguientes reglas:

•Tener un solo @ en una posición intermedia de la cadena (ni la primera ni la última letra)
•No contener dos puntos seguidos (uno a continuación del otro)
•No empezar ni terminar con un punto
"""

usuario = input('Usuario: ')
cant_arroba = 0
arroba_intermedia = True
punto_intermedio = True
dos_puntos = False
anterior = ''

if usuario[0] == '@' or usuario[-1] == '@':
    arroba_intermedia = False
if usuario[0] == '.' or usuario[-1] == '.':
    punto_intermedio = False

for char in usuario:
    if char == '@':
        cant_arroba += 1
    elif char == '.' and anterior == '.':
        dos_puntos = True

    anterior = char

if arroba_intermedia and punto_intermedio and not dos_puntos:
    print(f'El usuario {usuario} es valido.')
else:
    print('El usuario ingresado es invalido por las siguientes razones: ')
    if not arroba_intermedia:
        print('El usuario no puede empezar o terminar con arroba;')
    if cant_arroba != 1:
        print(f'Se han ingresado [{cant_arroba}] arrobas, se esperaba [1];')
    if not punto_intermedio:
        print('El usuario no puede empezar o terminar con punto;')
    if dos_puntos:
        print('El usuario no puede contener dos puntos consecutivos.')
