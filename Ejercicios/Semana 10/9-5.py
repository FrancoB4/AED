"""
Desarrollar un programa de Python que permita cargar por teclado un secuencia de números, uno por uno. Siempre se supone
que el usuario cargará un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un dato a
procesar. El programa debe:

    a) Determinar cuantos números se encuentran en el rango definido por 2 números p y q previamente ingresados (validar
     que los números que definen el rango son mayores a cero)

    b) Determinar la cantidad de veces que se ingresaron 2 números contiguos pares.

    c) Determinar la cantidad de números que son múltiplos del primer numero de la secuencia.

    d) Determinar el porcentaje que representa la cantidad del primer punto sobre el total de números de la secuencia.
"""
from aux_func.sequences import insert_sequence, insert_num
from aux_func.text_proces import percentage


def main():
    sequence = insert_sequence()
    n1, n2 = insert_num(text='Ingrese el menor de los números: '), insert_num(text='Ingrese el mayor de los números: ')

    in_range = pares_continuos = multip_primer_num = total_num = 0
    par = False

    firs_num = int(sequence[0])

    for char in sequence:
        total_num += 1
        num = int(char)

        if n1 <= num <= n2:
            in_range += 1

        if num % 2 == 0 and not par:
            par = True
        elif num % 2 == 0 and par:
            pares_continuos += 1
            par = False
        else:
            par = False

        if num % firs_num == 0:
            multip_primer_num += 1

    porcentaje = percentage(in_range, total_num)

    print(f'Dentro del rango especificado:          |{in_range}')
    print(f'Cantidad de números pares continuos:    |{pares_continuos}')
    print(f'Múltiplos del primer numero:            |{multip_primer_num}')
    print(f'Porcentaje de números en rango:         |{porcentaje}')


if __name__ == '__main__':
    main()
