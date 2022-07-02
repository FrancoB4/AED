"""Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe incluir
al menos una función simple con parámetros y retorno de resultado, debe procesar el texto caracter a caracter (a
razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

1 - Determinar la cantidad de palabras que tienen dos o más vocales (minúsculas o mayúsculas) y que no contienen ni
"q" ni "z"  (minúsculas o mayúsculas). Por ejemplo, en el texto: "Los cursos se evalúan con quiz." hay 2 palabras que
cumplen con la condición: "cursos" y "evalúan".

2 - Determinar la cantidad de palabras que tienen la segunda letra (minúscula o mayúscula) igual que su última letra
(minúscula o mayúscula). Por ejemplo, en el texto: "Hola casa azul." hay 1 palabra ("casa") que cumple con la
condición.

3 - Determinar cuántas palabras de longitud mayor a dos, empiezan con el segundo caracter de la primera palabra del
texto (en minúscula o en mayúscula). Por ejemplo, en el texto: "Para el alfil no hay alcance." hay dos palabras (
"alfil" y "alcance") que cumplen con la condición.

4 - Determinar la cantidad de palabras que contienen la expresión "pa" o "pA" (la "p" en minúscula) pero de forma que
la palabra no termine con esa expresión. Por ejemplo en el texto: "Se paran y se sacan la capA para no tener frío en
casa de Pablo.“, hay 2 palabras que cumplen con la condición: "paran" y "para". La palabra "Pablo" no cuenta porque
la "P" está en mayúscula, y la palabra "capA" tiene la secuencia pedida, pero no cuenta porque la palabra termina
ella. """
from aux_func.text_proces import *


def main():
    text = input('Ingrese un texto: ')

    pal_vocales_no_qz = pal_segunda_ultima = pal_2_empiezan_segundo = palabras_pa = 0
    vocales = orden = orden_pa = 0
    es_p = tiene_pa = com_seg_car = False
    no_q = no_z = True
    segundo_caracter_texto = segundo_caracter_palabra = None

    for char in text:
        if is_char(char):
            orden += 1

            if orden == 2:
                if segundo_caracter_texto is None:
                    segundo_caracter_texto = char.lower()
                if segundo_caracter_palabra is None:
                    segundo_caracter_palabra = char.lower()

            if is_vocal(char.lower()):
                vocales += 1

            if char.lower() == 'q':
                no_q = False
            if char.lower() == 'z':
                no_z = False

            if orden == 1 and char.lower() == segundo_caracter_texto:
                com_seg_car = True

            if char == 'p':
                es_p = True
            elif es_p and char.lower() == 'a':
                tiene_pa = True
                orden_pa = orden
                es_p = False
            else:
                es_p = False

            ultimo = char.lower()

        else:
            if vocales >= 2 and no_q and no_z:
                pal_vocales_no_qz += 1

            if com_seg_car and orden > 2:
                pal_2_empiezan_segundo += 1

            if segundo_caracter_palabra == ultimo:
                pal_segunda_ultima += 1

            if tiene_pa and orden != orden_pa:
                palabras_pa += 1

            orden = vocales = 0
            es_p = tiene_pa = com_seg_car = False
            no_q = no_z = True
            segundo_caracter_palabra = None

    print(f'Palabras con mas de una vocal sin "q" ni "z":       |{pal_vocales_no_qz}')
    print(f'Palabras cuyos segundo y ultimo car son iguales:    |{pal_segunda_ultima}')
    print(f'Palabras que empizan por el seg car del texto:      |{pal_2_empiezan_segundo}')
    print(f'Palabras que contienen "pa" o "pA" no en el fin:    |{palabras_pa}')


if __name__ == '__main__':
    main()
