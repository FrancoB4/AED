continuar = 'y'
dos = una = imaginaria = 0

while continuar == 'y':
    discriminante = float(input('Ingrese el un discriminante: '))

    if discriminante > 0:
        dos += 1
    elif discriminante == 0:
        una += 1
    else:
        imaginaria += 1

    continuar = input('Desea continuar (y/n): ')

print(f'Ingreso {dos} discriminantes con dos raíces.')
print(f'Ingreso {una} discriminantes con una raíz.')
print(f'Ingreso {imaginaria} discriminantes con raíces, lo que representa un '
      f'{round(imaginaria/(una + dos + imaginaria) * 100, 2)}% del total.')
