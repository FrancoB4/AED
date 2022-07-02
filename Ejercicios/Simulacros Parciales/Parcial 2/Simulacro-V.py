"""Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe incluir
al menos una función simple con parámetros y retorno de resultado, debe procesar el texto caracter a caracter (a
razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

1 - Determinar la cantidad de palabras con 3 o más caracteres de largo, que contienen los dígitos "1" y "4" en
cualquier orden. Por ejemplo, en el texto: "El vehículo dominio HKV154 tiene 14 multas." hay 1 palabra que debe
contarse ("HKV154"). La palabra "14" no cuenta porque tiene menos de tres caracteres (aunque tiene los dígitos "1" y
"4").

2 - Determinar el porcentaje que representan las palabras que comienzan con el primer caracter del texto,
(en minúscula o mayúscula) sobre el total de palabras. Por ejemplo, en el texto: "En este año estaremos mejor." hay 3
palabras que cumplen la condición ("En", "este" y "estaremos") sobre un total de 5 palabras. El porcentaje entonces
es 60%.

3 - Determinar si existen palabras que no tengan letras "o" (minúsculas o mayúsculas). Por ejemplo, en el texto: "Ojo
con nuestro oso." no hay palabras sin la letra "o", por lo que el resultado aquí debe ser un mensaje de la forma "No
hay palabras sin 'o'". Y si el texto fuese: "Para la duda máxima." entonces el resultado debería ser un mensaje de la
forma "Hay palabras sin 'o'".

4 - Determinar el promedio de letras por palabra de aquellas en las que se presenta solo una vez la expresión "al" (
con cualquiera de sus letras en minúscula o en mayúscula). Por ejemplo, en el texto: "El ala derecha tiene algunos
defectos." hay 2 palabras con una sola expresión "al" ("ala" y "algunos") y suman 10 letras entre ambas. El promedio
pedido entonces es 5. """
from aux_func.text_proces import *


def main():
    text = input('ingrese un texto: ').lower()

    pal_3_car_14 = total_palabras = palabras_o = total_letras_al = pal_com_prim_car = palabras_al = 0
    orden = cantidad_al = 0
    uno = cuatro = es_a = tiene_o = False
    primr_caracter = None

    for char in text:
        if is_char(char):
            orden += 1

            if primr_caracter is None:
                primr_caracter = char

            if char == '1':
                uno = True
            elif char == '4':
                cuatro = True

            if orden == 1 and char == primr_caracter:
                pal_com_prim_car += 1

            if char == 'o':
                tiene_o = True

            if char == 'a':
                es_a = True
            elif es_a and char == 'l':
                cantidad_al += 1
                es_a = False
            else:
                es_a = False

        else:
            total_palabras += 1

            if orden >= 3 and uno and cuatro:
                pal_3_car_14 += 1

            if tiene_o:
                palabras_o += 1

            if cantidad_al == 1:
                total_letras_al += orden
                palabras_al += 1

            orden = cantidad_al = 0
            uno = cuatro = es_a = False

    porc = percentage(pal_com_prim_car, total_palabras)
    prom = average(total_letras_al, palabras_al)

    print(f'Palabras 3 o mas car que contienen "1" y "4":           |{pal_3_car_14}')
    print(f'Porcentaje de palabras que comienzan con el primer car: |{porc}%')
    if palabras_o == total_palabras:
        print(f'No hay palabras "o".')
    else:
        print('Hay palabras sin "o".')
    print(f'Promedio de letras palabras al:                         |{prom}')


if __name__ == '__main__':
    main()
