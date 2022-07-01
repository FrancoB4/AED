"""
Desarrollar un programa en Python que permita cargar por teclado una sucesión de números, uno por uno. Siempre se supone
 que el usuario cargará un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un dato a
 procesar. El programa debe:

a) Determinar cuántos de los números ingresados eran mayores que n1 y menores que n2 (cargar previamente por teclado los
 números n1 y n2).

b) Determinar el porcentaje que el total de números calculado en el punto 1 representa en el total de números cargados.

c) Determinar si en algún momento se ingresó un número impar seguido inmediatamente de un par. No importa cuántas
veces ocurrió: sólo indicar si al menos una vez pasó.

d) Determinar cuántas veces se ingresó un 5 seguido inmediatamente de otro 5. Por ejemplo: en la sucesión: 3, 6, 5, 5,
7, 5, 2, 5, 9, 5, 5, 0 ocurrió dos veces.
"""
from aux_func.sequences import insert_sequence
from aux_func.text_proces import percentage


def main():
    sequence = insert_sequence()
    n1, n2 = int(input('N1: ')), int(input('N2: '))

    may_n1_men_n2 = cant_num = cant_five = 0
    impar = impar_par = five = False

    for char in sequence:
        cant_num += 1
        num = int(char)

        if n1 < num < n2:
            may_n1_men_n2 += 1

        if num % 2 != 0:
            impar = True
        elif impar and num % 2 == 0:
            impar_par = True
        else:
            impar = False

        if num == 5 and not five:
            five = True
        elif five and num == 5:
            cant_five += 1
            five = False
        else:
            five = False

    porcentaje = percentage(may_n1_men_n2, cant_num)

    print(f'Mayores que {n1} y menores que {n2}:        | {may_n1_men_n2}')
    print(f'Porcentaje may {n1} y men {n2}:             | {porcentaje}')
    print(f'Impares seguidos por pares:             | {impar_par}')
    print(f'Cantidad doble cinco en la secuencia:   | {cant_five}')


if __name__ == '__main__':
    main()
