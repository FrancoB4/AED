"""Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe incluir
al menos una función simple con parámetros y retorno de resultado, debe procesar el texto caracter a caracter (a
razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:


1- Determinar la cantidad de palabras que tienen dos o más dígitos y contienen también una "k" (minúscula o
mayúscula) o una "r" (minúscula o mayúscula). Por ejemplo, en el texto “Los cursos que se presentan son el 1K04 y el
1R11.” Resultado: 2 palabras cumplen con la condición (“1K04” y “1R11”).

2 - Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que tienen más consonantes que
vocales. Por ejemplo, en el texto: "El ciclo es infinito." hay 4 palabras en total, y solo una ("ciclo") tiene más
consonantes que vocales. Por lo tanto, el porcentaje pedido es del 25%.

3 - Determinar cuántas palabras contienen entre sus tres primeras posiciones al primer caracter de la primera palabra
del texto (en minúscula o en mayúscula). Por ejemplo, en el texto: "Por cada pibe que aprueba exceptuamos un final."
la primera palabra comienza con 'P' y hay entonces tres palabras que cumplen la condición (incluida la misma primera
palabra): "Por", "pibe" y "aprueba".  La palabra "exceptuamos" no cumple porque si bien contiene una "p", la misma no
está entre las tres primeras posiciones.

4 - Determinar la cantidad de palabras que contienen la expresión "se" (con cualquiera de sus letras en minúscula o
en mayúscula) pero de forma que la palabra NO COMIENCE con esa expresión. Por ejemplo en el texto: “Se separa y pasea
para moverse un poco.“, las palabras “pasea” y “moverse” cumplen con la condición. Notar que "Se" y "separa"
contienen “se” pero ambas comienzan con "se" y por lo tanto no deben ser contadas. """
from aux_func.text_proces import *


def main():
    text = input('Ingrese un texto: ').lower()

    dos_num_k_r = total_palabras = mas_cons_vocales = pal_prim_caracter = palabras_se = 0
    numeros = vocales = consonantes = orden = 0
    tiene_prim_car = es_s = tiene_k_o_r = tiene_se = False
    primer_caracter = None

    for char in text:
        if is_char(char):
            orden += 1

            if primer_caracter is None:
                primer_caracter = char

            if is_num(char):
                numeros += 1

            if is_vocal(char):
                vocales += 1

            if not is_vocal(char):
                consonantes += 1

            if char in 'kr':
                tiene_k_o_r = True

            if total_palabras != 0 and char == primer_caracter and orden <= 3:
                tiene_prim_car = True

            if char == 's' and orden != 1:
                es_s = True
            elif es_s and char == 'e':
                tiene_se = True
                es_s = False
            else:
                es_s = False

        else:
            total_palabras += 1

            if numeros >= 2 and tiene_k_o_r:
                dos_num_k_r += 1

            if vocales < consonantes:
                mas_cons_vocales += 1

            if tiene_se:
                palabras_se += 1

            if tiene_prim_car or total_palabras == 1:
                pal_prim_caracter += 1

            numeros = vocales = consonantes = orden = 0
            tiene_prim_car = es_s = tiene_k_o_r = tiene_se = False

    prom = percentage(mas_cons_vocales, total_palabras)

    print(f'Palabras con dos o mas num y "k" o "r":     |{dos_num_k_r}')
    print(f'Promedio mas consonantes que vocales:       |{prom}')
    print(f'Palabras que contienen el primer caracter:  |{pal_prim_caracter}')
    print(f'Palabras que contienen "se":                |{palabras_se}')


if __name__ == '__main__':
    main()
