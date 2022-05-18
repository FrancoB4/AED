"""
Desarrolle un programa completo en Python que permita generar una sucesión de 5000 números enteros aleatorios, usando
como semilla del generador el número 76. Los valores de cada uno de esos 5000 números deben estar entre 1 y 65000
(incluidos ambos). A partir de esa sucesión el programa debe:

1 - Determinar la cantidad de números pares que sean múltiplos de 6
2 - Determinar la cantidad de números son mayores del primer número de la serie, no incluir dicho número
3 - Determinar la cantidad de números que perteneces al segundo millar de números
4 - Determinar el porcentaje que representan la cantidad de números del punto 2 respecto del total de números procesados
"""
import random
random.seed(76)

mult_6 = may_primero = segundo_millar = 0

for i in range(5000):
    num = random.randint(1, 65000)

    if i == 0:
        primero = num

    if num % 6 == 0:
        mult_6 += 1

    if i > 0 and num > primero:
        may_primero += 1

    if 2000 <= num < 3000:
        segundo_millar += 1

print(f'Múltiplos pares de 6: {mult_6}')
print(f'Mayores que el primero: {may_primero}')
print(f'Pertenecientes al segundo millar: {segundo_millar}')
print(f'El porcentaje que representan los números mayores que el primero sobre '
      f'el total es del: {may_primero / 5000 * 100}%')
