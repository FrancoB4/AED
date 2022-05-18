"""
Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas por sus vendedores, para ello le
solicita un sistemita que le permita calcular dicho montos.

Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores (1 a 4). Usted debe solicitar el ingreso de
la categoría del vendedor y el total de la venta (el proceso termina cuando se ingrese una categoría igual a cero) y
acumular las comisiones de las ventas rendidas por los vendedores de diferentes en base a los siguientes cálculos:

a) Categoría 1: cobra una comisión de 10%
b) Categoría 2: cobra una comisión de 25%
c) Categoría 3: cobra una comisión de 30%
d) Categoría 4: cobra una comisión de 40%

Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría de vendedores que tiene
la empresa junto con el total general
"""
c1 = c2 = c3 = c4 = 0

categoria = int(input('Ingrese la categoría de vendedor: '))

while categoria != 0:
    venta = float(input('Ingrese el monto de la venta: '))
    if categoria == 1:
        c1 += venta
    if categoria == 2:
        c2 += venta
    if categoria == 3:
        c3 += venta
    if categoria == 4:
        c4 += venta

    categoria = int(input('Ingrese la categoría de vendedor: '))

print(f'Comisiones categoría 1: {c1/100*10}\nComisiones categoría 2: {c2/100*25}')
print(f'Comisiones categoría 3: {c3/100*30}\nComisiones categoría 4: {c2/100*40}')
