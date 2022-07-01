"""Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe incluir
al menos una función simple con parámetros y retorno de resultado, debe procesar el texto caracter a caracter (a
razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

1 - Determinar la cantidad de palabras que tienen dos o más vocales pero no contienen una "s" (minúscula o
mayúscula). Por ejemplo, en el texto “Los estudiantes rinden el parcial.” hay 2 palabras que cumplen con la condición
("rinden" y "parcial").

2 - Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que finalizan en una
consonante. Por ejemplo, en el texto: "El cielo es celeste." hay 4 palabras en total, y sólo 2 ("El" y "es") tienen
una consonante como última letra. Por lo tanto, el porcentaje pedido es del 50%.

3 - Determinar cuántas palabras contienen (pero sin empezar con él) al último caracter de la primera palabra del
texto (en minúscula o en mayúscula). Por ejemplo, en el texto: "Bienvenidos son los alumnos." la primera palabra
finaliza con 's' y hay entonces 2 palabras que contienen a esa letra sin comenzar con ella ("los" y "alumnos"). La
palabra "son" contiene una "s", pero comienza con ella, y, por lo tanto, no debe ser contada.

4 - Determinar la cantidad de palabras que contienen la expresión "mi" (con cualquiera de sus letras en minúscula o
en mayúscula) pero de forma que la palabra COMIENCE con esa expresión. Por ejemplo en el texto: “Mis amigos son
miles.“, las palabras "Mis" y "miles" cumplen con la condición. Notar que "amigos" contiene "mi" pero no al inicio y,
por lo tanto, no debe ser contada. """
from aux_func.text_proces import *


def main():
    texto = input('Ingrese un texto: ').lower()

    palabras_vocales_s = termina_consonante = palabras_ultimo_car = total_palabras = palabras_mi = 0
    vocales = orden = 0
    tiene_s = es_m = tiene_ultim_car = consonante = tiene_mi = False
    ultimo_caracter = None

    for car in texto:
        if is_char(car):
            orden += 1

            if car == 's':
                tiene_s = True

            if is_vocal(car):
                vocales += 1

            if not is_vocal(car):
                consonante = True
            else:
                consonante = False

            if ultimo_caracter is not None and car == ultimo_caracter and orden != 1:
                tiene_ultim_car = True

            if car == 'm' and orden == 1:
                es_m = True
            elif es_m and car == 'i':
                tiene_mi = True
                es_m = False
            else:
                es_m = False

            anterior = car
        else:
            total_palabras += 1

            if not tiene_s and vocales >= 2:
                palabras_vocales_s += 1

            if consonante:
                termina_consonante += 1

            if ultimo_caracter is None:
                ultimo_caracter = anterior

            if tiene_ultim_car:
                palabras_ultimo_car += 1

            if tiene_mi:
                palabras_mi += 1

            vocales = orden = 0
            tiene_s = es_m = tiene_ultim_car = consonante = tiene_mi = False

    porcentaje_fin_consonante = percentage(termina_consonante, total_palabras)

    print(f'Palabras dos o mas vocales sin s:                   | {palabras_vocales_s}')
    print(f'Porcentaje termina en consonante:                   | {porcentaje_fin_consonante}%')
    print(f'Palabras que contienen el ult car de la primera:    | {palabras_ultimo_car}')
    print(f'Palabras contienen "mi":                            | {palabras_mi}')


if __name__ == '__main__':
    main()
