num = int(input('Ingrese el primer numero de la serie: '))
cont = 0
may = 0

while num != 0:
    if num > may and cont % 2 == 0:
        may = num

    num = int(input('Ingrese el siguiente numero de la serie: '))

print(f'El mayor número de la serie, de orden par, es: {may}')
