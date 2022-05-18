"""
Cargar por teclado n números enteros positivos, uno a uno. Se deberá establecer qué número es el mayor de los números
pares y el menor de los números impares.

Por ejemplo, en una secuencia de números: 8, 15, 9, 2, 27, 18, 0; el mayor de los pares sería el número 18 y el menor
de los impares el número 9.
"""

may_pares = 0
men_impares = 0
imp = 0
n = int(input('Ingrese n: '))

for i in range(1, n + 1):
    num = int(input(f'Ingrese el numero {i}: '))

    if num % 2 == 0 and num > may_pares:
        may_pares = num
    elif num % 2 != 0:
        if imp == 0:
            men_impares = num
        elif num < men_impares:
            men_impares = num

        imp += 1

print(f'El mayor de los números pares ingresados fue: {may_pares}')
print(f'El menor de los números impares ingresados fue: {men_impares}')
