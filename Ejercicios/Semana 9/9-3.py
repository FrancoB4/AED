"""
Desarrolle un programa completo en Python que permita generar una sucesión de 20000 números enteros aleatorios, usando
como semilla del generador el numero 49 (es decir random.seed(49)). Los valores de cada uno de esos 20000 números deben
estar entre 1 y 45000 (incluidos ambos) (DEBE usar random.randint(1, 45000) para generar esos números). A partir de esa
sucesión el programa debe:

* Indicar cuantos números eran múltiplos de 5, cuántos eran múltiplos de 7 y cuántos eran múltiplos de 9.
* Indicar el mayor entre todos aquellos números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8.
* Indicar cuantos números generados son pares menores a 15000.
* Indicar el porcentaje entero que representa el punto anterior sobre el total de números procesados. Aclaración 1: NO
se pide el porcentaje redondeado, sino el porcentaje truncado, sin decimales. Aclaración 2: en el cálculo de este
porcentaje, haga primero la multiplicación que corresponda, y luego la división.
"""
import random
random.seed(49)

mult_5 = mult_7 = mult_9 = par_men_15000 = ultimo_may_5_men_8 = 0

for i in range(20000):
    num = random.randint(1, 45000)

    if num % 5 == 0:
        mult_5 += 1
    if num % 7 == 0:
        mult_7 += 1
    if num % 9 == 0:
        mult_9 += 1

    if 3 > num % 5 > 0 and num % 10 != 0:
        ultimo_may_5_men_8 += 1

    if num % 2 == 0 and num < 15000:
        par_men_15000 += 1

print(f'Múltiplos de 5: {mult_5}')
print(f'Múltiplos de 7: {mult_7}')
print(f'Múltiplos de 9: {mult_9}')
print(f'Números con el ultimo digito mayor que 5 y menor que 8: {ultimo_may_5_men_8}')
print(f'Pares menores que 15000: {par_men_15000}')
pares_men_15000_pc = par_men_15000 * 100
porcentaje = int(pares_men_15000_pc / 20000)
print(f'El porcentaje que representan los números pares menores a 15000 sobre el total es del {porcentaje}%')
