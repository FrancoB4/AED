def insert_sequence(end_char='0'):
    sequence = num = ''
    while num != '0':
        num = input('Ingrese un numero: ')
        if num != '0':
            sequence += num

    return sequence
