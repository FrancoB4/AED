seguir = 's'
while seguir == 's' or seguir == 'S':

    # titulo y carga de datos...
    print('Raíces de la ecuación de segundo grado...')
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

    # procesos: aplicar directamente las fórmulas...
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

    # visualización de resultaddos...
    print('x1:', x1)
    print('x2:', x2)

    seguir = input('Desea resolver otra ecuacion? (s/n): ')

print('Gracias por utilizar nuestro programa...')