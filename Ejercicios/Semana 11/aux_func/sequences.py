def insert_sequence(end_char='0'):
    sequence = num = ''
    while num != '0':
        num = input('Ingrese un numero: ')
        if num != '0':
            sequence += num

    return sequence


def insert_num(text='Ingrese un numero: '):
    num = 0
    while num <= 0:
        num = int(input(text))
        if num <= 0:
            print('Ingrese un valor mayor que cero.')

    return num
