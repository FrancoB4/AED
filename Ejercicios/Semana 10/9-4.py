"""
Desarrollar un programa en Python que permita cargar por teclado un texto. Siempre se supone que usuario cargará un
punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en
blanco.

El programa debe determinar:
    a) La cantidad de palabras que comienzan con la expresión "pa" y termina con la letra "n"

    c) La cantidad de palabras que presentan mas de dos vocales a partir de la tercera letra de la palabra

    d) El porcentaje que representa la cantidad de palabras del punto anterior respecto de la cantidad de total de
    palabras del texto

    e) Cantidad de palabras de mas de 5 letras
"""
from aux_func.text_proces import is_char, is_vocal, percentage


def main():
    text = input('Ingrese un texto: ')

    pa_n = mas_dos_vocales = total_palabras = palabras_mas_5_letras = count = vocals_after_3 = 0

    p = comienza_pa = False

    for char in text:
        if is_char(char):
            count += 1

            if char == 'p' and count == 1:
                p = True
            elif p and char == 'a':
                comienza_pa = True
                p = False
            else:
                p = False

            if count > 3 and is_vocal(char):
                vocals_after_3 += 1

            anterior = char
        else:
            total_palabras += 1

            if comienza_pa and anterior == 'n':
                pa_n += 1

            if vocals_after_3 > 2:
                mas_dos_vocales += 1

            if count > 5:
                palabras_mas_5_letras += 1

            vocals_after_3 = count = 0
            p = comienza_pa = False

    porcentaje = percentage(mas_dos_vocales, total_palabras)

    print(f'Palabras comenzadas con pa y terminadas en n:       |{pa_n}')
    print(f'Mas de dos vocales después de la tercera letra:     |{mas_dos_vocales}')
    print(f'Porcentaje del punto anterior sobre el total:       |{porcentaje}')
    print(f'Palabras con mas de cinco letras:                   |{palabras_mas_5_letras}')


if __name__ == '__main__':
    main()
