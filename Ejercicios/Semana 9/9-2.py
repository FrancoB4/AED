"""
Generar una secuencia de n números aleatorios. El valor de n se ingresa por teclado, validar que sea mayor a 0.

Determinar:

a) Cuántos números terminan en 5.

b) El porcentaje de números pares en la secuencia.

c) Cual es el menor número múltiplo de 3 de la secuencia.

d) La cantidad de veces que aparece el primer número de la secuencia.
"""
import random

ter_5 = pares = men_mult_3 = veces_primero = 0

n = 0
while n <= 0:
    n = int(input('Ingrese n: '))
    if n <= 0:
        print('Ingrese un valor mayor que 0')

for i in range(n):
    num = random.randint(1, 10000)

    if i == 0:
        primero = num

    if num % 5 == 0 and num % 10 != 0:
        ter_5 += 1

    if num % 2 == 0:
        pares += 1

    if num % 3 == 0 and (men_mult_3 == 0 or num < men_mult_3):
        men_mult_3 = num

    if num == primero and i != 0:
        veces_primero += 1

print(f'Números terminados en 5: {ter_5}')
print(f'Porcentaje de números pares: {round(pares / n * 100, 2)}')
print(f'Menor múltiplo de 3: {men_mult_3}')
print(f'Veces que apareció el primer valor de la secuencia: {veces_primero}')
