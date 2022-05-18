"""
Ingresar una secuencia de n números, de a uno por vez. El valor de n se ingresa por teclado, validar que sea mayor a 0.
Determinar:

a) Cuántos números ingresados terminan en 5

b) La cantidad de veces que aparece el primer número ingresado por el usuario en la secuencia

c) Cuántos números ingresados son mayores al anterior
"""

termina_cinco = 0
veces_primer_numero = 0
may_anterior = 0

n = int(input('n: '))

for i in range(1, n + 1):
    num = int(input(f'Numero {i}: '))
    while num <= 0:
        num = int(input('Ingrese un valor mayor que cero: '))

    if i == 1:
        primer_numero = num
        anterior = num

    if num % 5 == 0 and num % 10 != 0:
        termina_cinco += 1

    if num == primer_numero:
        veces_primer_numero += 1

    if num > anterior:
        may_anterior += 1

    anterior = num

print(f'Números terminados en 5: {termina_cinco}')
print(f'Veces que salio el primer número: {veces_primer_numero}')
print(f'Números ingresados mayores que el anterior: {may_anterior}')
