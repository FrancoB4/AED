"""Desarrollar un programa en Python que permita cargar por teclado un texto completo (analizar dos opciones: una es
cargar todo el texto en una variable de tipo cadena de caracteres y recorrerla con un for iterador; y la otra es
cargar cada caracter uno por uno a través de un while). Siempre se supone que el usuario cargará un punto para
indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El
programa debe:

a) Determinar cuántas palabras tenían más de 4 letras.

b) Determinar cuántas palabras tenían al menos una vez la letra "x" o la letra "y".

c) Determinar el promedio de letras por palabra en todo el texto.

d) Determinar cuántas palabras contuvieron sólo una vez la expresión "mo".

********************************************************************************
Ejemplo: 'el mono momoxy toca el xilofón.'
********************************************************************************
Palabras con más de 4 letras: 2
Palabras tenían al menos una vez la letra "x" o la letra "y": 2
El promedio de letras por palabra en todo el texto es: 4.17
Determinar cuántas palabras contuvieron sólo una vez la expresión "mo": 1
"""
from aux_func.text_proces import average, is_char


def main():
    palabras_mas_4_car = palabras_x_y = total_caracteres = total_palabras = palabras_mo = c_car = 0
    m = x_y = False
    mo = None

    text = input('Ingrese el texto: ')

    for char in text:
        if is_char(char):
            c_car += 1

            if char in 'xy':
                x_y = True

            if char == 'm':
                m = True
            elif m and char == 'o':
                if mo is None:
                    mo = True
                else:
                    mo = False
            elif m:
                m = False

        else:
            if c_car >= 4:
                palabras_mas_4_car += 1

            if x_y:
                palabras_x_y += 1

            if mo:
                palabras_mo += 1

            total_caracteres += c_car
            total_palabras += 1

            c_car = 0
            x_y = m = False
            mo = None

    promedio_car_palabra = average(total_caracteres, total_palabras)

    print(f'Palabras con mas de 4 caracteres:  | {palabras_mas_4_car}')
    print(f'Palabras con x o y:                | {palabras_x_y}')
    print(f'Promedio de letras por palabra:    | {promedio_car_palabra}')
    print(f'Palabras con silaba mo una vez:    | {palabras_mo}')


if __name__ == '__main__':
    main()
