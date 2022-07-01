"""Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe incluir
al menos una función simple con parámetros y retorno de resultado, debe procesar el texto caracter a caracter (a
razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

1- Determinar la cantidad de palabras que tienen dos o más vocales (minúsculas o mayúsculas) y que contienen también
una letra "m" (minúscula o mayúscula). Por ejemplo, en el texto "Todos estamos muy esperanzados." hay 1 palabra que
cumple con la condición ("estamos").

2- Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que tienen más dígitos que
vocales (mayúsculas o minúsculas). Por ejemplo, en el texto "Los códigos 312ABZ y YAA123 de autopartes tienen stock."
hay 9 palabras y dos de ellas cumplen la condición, por lo que el porcentaje pedido es: 22.22%.

3 - Determinar cuántas palabras tienen una "c" (mayúscula o minúscula) entre las dos primeras posiciones de la
palabra y además contienen una "b" o una "d" (ambas en minúscula o en mayúscula) en cualquier otra posición (pero no
entre las dos primeras). Por ejemplo, en el texto "El club está cerrado." hay 2 palabras que cumplen la condición  (
"club" y "cerrado").

4 - Determinar cuántas palabras del texto contienen la expresión "ta" (con cualquiera de sus letras en minúscula o en
mayúscula) dos o más veces en cualquier parte de la palabra. Por ejemplo, en el texto "La tarta viene bien para la
tarde." hay 1 palabra cumple con la condición ("tarta"). La palabra "tarde" tiene la expresión "ta" pero solo una
vez, y, por lo tanto, no debe ser contada. """
from aux_func.text_proces import *


def main():
    text = input('Ingrese un texto: ').lower()

    mas_num_que_vocales = palabras_vocales_m = palabras_c_bd = palabras_ta = total_palabras = 0
    vocales = numeros = orden = cantidad_ta = 0
    es_t = primeras_c = tiene_b_d = tiene_m = False

    for char in text:
        if is_char(char):
            orden += 1
            if is_vocal(char):
                vocales += 1

            if char == 'm':
                tiene_m = True

            if is_num(char):
                numeros += 1

            if orden <= 2 and char == 'c':
                primeras_c = True
            elif orden > 2 and primeras_c and char in 'bd':
                tiene_b_d = True

            if char == 't':
                es_t = True
            elif es_t and char == 'a':
                cantidad_ta += 1
                es_t = False
            else:
                es_t = False
        else:
            total_palabras += 1

            if numeros > vocales:
                mas_num_que_vocales += 1

            if vocales >= 2 and tiene_m:
                palabras_vocales_m += 1

            if primeras_c and tiene_b_d:
                palabras_c_bd += 1

            if cantidad_ta >= 2:
                palabras_ta += 1

            vocales = numeros = orden = cantidad_ta = 0
            es_t = primeras_c = tiene_m = tiene_b_d = False

    porc_mas_num_que_vocales = percentage(mas_num_que_vocales, total_palabras)

    print(f'Dos o mas vocales y "m":                | {palabras_vocales_m}')
    print(f'Porcentaje mas números que vocales:     | {porc_mas_num_que_vocales}%')
    print(f'Tiene "c" entre las primeras y b o d:   | {palabras_c_bd}')
    print(f'Tiene "ta" mas de una vez:              | {palabras_ta}')


if __name__ == '__main__':
    main()
