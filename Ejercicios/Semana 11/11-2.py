"""
Desarrollar un programa de Phyton que permita cargar por teclado una secuencia de números, uno por uno. Siempre se
supone que el usuario cargará un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un
dato a procesar. El programa debe:

    a) Determinar el porcentaje que cantidad de números pares representa en la cantidad total de números ingresados.

    b) Determinar cuántos de los números ingresados tenían su último dígito igual a 4 o igual a 5.

    c) Determinar el menor de los números ingresados que sean divisibles por 3.

    d) Determinar si la secuencia estaba formada sólo por números menores o iguales que 7.
"""
from aux_func.sequences import insert_sequence


def main():
    sequence = insert_sequence()

    total_numeros = pares = ult_4_5 = menor_mult_3 = 0

    for char in sequence:
        num = int(char)


if __name__ == '__main__':
    main()
