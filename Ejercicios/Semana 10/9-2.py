"""
Desarrollar un programa en Python que permita cargar por teclado una sucesión de números, uno por uno. Siempre se supone
que el usuario cargará un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un dato a
procesar. El programa debe:

a) Determinar cuántos de los números ingresados eran divisibles por 4.

b) Determinar el mayor de los números impares ingresados.

c) Determinar cuántas veces se ingresó el primero de los números (cuente al primero).

d) Determinar cuántas veces se ingresó un 1, seguido de un 2, y seguido a su vez de un 3. Por ejemplo: en la sucesión:
3, 6, 1, 2, 3, 7, 8, 2, 3, 1, 2, 3, 0 ocurrió dos veces.
"""
from aux_func.text_proces import is_num


def main():
    div_4 = may = veces_prim = veces_123 = 0
    one = one_two = False

    text = num = ''
    while num != '0':
        num = input('Ingrese un numero: ')
        if num != '0':
            text += num

    first = text[0]

    for char in text:
        if char == first:
            veces_prim += 1

        if char == '1':
            one = True
        elif one and char == '2':
            one_two = True
        elif one_two and char == '3':
            veces_123 += 1
            one = one_two = False
        else:
            one = one_two = False

        if is_num(char):
            num = int(char)

            if num % 4 == 0:
                div_4 += 1

            if num > may:
                may = num

    print(f'Números divisibles por 4:       |{div_4}')
    print(f'Mayor de los números:           |{may}')
    print(f'Veces que salio el primero:     |{veces_prim}')
    print(f'Veces que apareció "123":       |{veces_123}')


if __name__ == '__main__':
    main()
