"""
Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. Se supone que el usuario cargará un punto para indicar el final del texto, y que cada palabra de
ese texto está separada de las demás por un espacio en blanco. El programa debe:


a) Determinar cuántas palabras tienen 3, 5 o 7 letras.

b) Determinar la cantidad de palabras con más de tres letras, que tienen una vocal en la tercera letra.

c) Determinar el porcentaje de palabras que tienen sólo una o dos vocales sobre el total de palabras del texto.

d) Determinar la cantidad de palabras que contienen más de una vez la sílaba "pe".
"""
from aux_func.text_proces import is_char, percentage, is_vocal


def main():
    text = input('Ingrese un texto: ')

    tienen_5_6_7 = mas_3_letras_vocal = una_o_dos_vocales = total_palabras = pe = mas_de_una_pe = count = vocals = 0
    p = vocal_pos_3 = False

    for char in text:
        if is_char(char):
            count += 1

            if is_vocal(char):
                if count == 3:
                    vocal_pos_3 = True
                vocals += 1

            if char == 'p':
                p = True
            elif p and char == 'e':
                pe += 1
                p = False
            else:
                p = False
        else:
            total_palabras += 1
            if count in (3, 5, 7):
                tienen_5_6_7 += 1

            if count > 3 and vocal_pos_3:
                mas_3_letras_vocal += 1

            if 1 <= vocals <= 2:
                una_o_dos_vocales += 1

            if pe > 1:
                mas_de_una_pe += 1

            count = vocals = pe = 0
            p = vocal_pos_3 = False

    porcentaje = percentage(una_o_dos_vocales, total_palabras)

    print(f'Palabras con 3, 5, o 7 letras:      |{tienen_5_6_7}')
    print(f'Mas de 3 letras con tercera vocal:  |{mas_3_letras_vocal}')
    print(f'Porcentaje una o dos vocales:       |{porcentaje}')
    print(f'Mas de una silaba "pe":             |{mas_de_una_pe}')


if __name__ == '__main__':
    main()
