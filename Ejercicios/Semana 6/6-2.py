"""
Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas en las diferentes sucursales
de un país de una determinada empresa.

Los requerimientos funcionales del programa son:

a) Informar la cantidad de ventas ingresadas.

b) Total de ventas.

c) Cantidad de ventas cuyo valor esté comprendido entre 100 y 300 unidades.

d) Cantidad de ventas con 400, 500 y 600 unidades.

e) Indicar si hubo una cantidad de ventas inferior a 50 unidades.

Usted deberá ingresar cantidades de ventas hasta que se ingrese un valor negativo.
"""
ventas = 0
total = 0
r1 = 0
r2 = 0
menos_50 = False

venta = int(input('Ingrese el tamaño de la primer venta: '))

while venta >= 0:
    ventas += 1
    total += venta

    if venta < 50:
        menos_50 = True

    if 100 < venta < 300:
        r1 += 1
    elif venta == 400 or venta == 500 or venta == 600:
        r2 += 1

    venta = int(input('Ingrese el tamaño de la siguiente venta: '))

print(f'Se han ingresado {ventas} ventas.')
print(f'Por un total de {total} unidades.')
print(f'Con {r1} ventas de entre 100 y 300 unidades. Y {r2} de 400, 500 o 600 unidades.')
if menos_50:
    print('Han existido ventas por menos de 50 unidades.')
else:
    print('No se han ingresado ventas por menos de 50 unidades.')
