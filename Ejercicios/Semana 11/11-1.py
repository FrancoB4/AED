"""
Desarrollar un programa en Python que permita cargar por teclado un texto completo. Siempre se supone que el usuario
cargará un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un
espacio en blanco. El programa debe:

a) Determinar cuántas palabras tenían al menos un caracter que era en realidad un dígito (un caracter entre '0' y '9').

b) Determinar cuántas palabras tenían 3 o menos letras, cuántas tenían 4 y hasta 6 letras, y cuántas tenían más de 6
letras.

c) Determinar la longitud de la palabra más larga del texto.

d) Determinar cuántas palabras contuvieron la expresión "de", pero en la primera mitad de la palabra.
"""
from aux_func.text_proces import is_char, is_num


def main():
    text = input('Inserte un texto: ')

    count = max_len = de_primera_mitad = tres_o_men = cuatro_a_seis = mas_seis = digito = pos_de = 0
    contiene_num = d = de = False

    for char in text:
        if is_char(char):
            count += 1
            if is_num(char):
                contiene_num = True

            if char == 'd' and not de:
                d = True
            elif d and char == 'e':
                pos_de = count
                de = True
                d = False
            else:
                d = False
        else:
            if contiene_num:
                digito += 1

            if count <= 3:
                tres_o_men += 1
            elif 4 <= count <= 6:
                cuatro_a_seis += 1
            elif count > 6:
                mas_seis += 1

            if count > max_len:
                max_len = count

            if de and pos_de > count / 2:
                de_primera_mitad += 1

            contiene_num = d = de = False
            count = pos_de = 0

    print(f'Contiene digito:         |{digito}')
    print(f'Longitud 3 o menos:      |{tres_o_men}')
    print(f'Longitud entre 4 y 6:    |{cuatro_a_seis}')
    print(f'Longitud mayor a 6:      |{mas_seis}')
    print(f'Longitud maxima:         |{max_len}')
    print(f'"de" en la primer mitad: |{de_primera_mitad}')


if __name__ == '__main__':
    main()
