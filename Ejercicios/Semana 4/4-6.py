"""
Se pide un programa que le solicite al usuario que ingrese una palabra. Con esa palabra calcular los siguientes puntos:

Determinar la cantidad de letras que tiene  la palabra.
Mostrar un mensaje que informe si la palabra termina en vocal.
"""

word = input('Ingrese la palabra: ')
last_char = word[::-1][0]

print(f'Cantidad de letras: {len(word)}')

if last_char == 'a' or last_char == 'e' or last_char == 'i' or last_char == 'o' or last_char == 'u':
    print('La palabra termina en vocal')
else:
    print('La palabra no termina en vocal')
