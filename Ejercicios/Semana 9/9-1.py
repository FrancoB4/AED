"""
Desarrolle un programa que permita generar una sucesión de mil números enteros aleatorios, usando como semilla del
generador al valor 11. Los números generados deben estar entre 1 y 2500 (ambos incluidos). A partir de esa sucesión, el
programa debe informar:

Cuántos números eran divisibles por 4 pero no por 8, y cuántos eran divisibles por ambos
El promedio de los valores mayores a 2000
Cuántos números eran menores al primer valor generado y qué porcentaje representan sobre el total de números
Si alguna vez aparecieron en la secuencia los valores extremos del intervalo (1, 2500)
"""
import random
random.seed(11)

div_4 = 0
div_4_8 = 0
may_2000 = 0
men_primero = 0
total_may_2000 = 0
extremos = False

for i in range(1000):
    n = random.randint(1, 2500)

    if i == 0:
        primero = n

    if n % 4 == 0 and n % 8 != 0:
        div_4 += 1
    elif n % 4 == 0 and n % 8 == 0:
        div_4_8 += 1

    if n > 2000:
        may_2000 += 1
        total_may_2000 += n

    if n < primero:
        men_primero += 1

    if n == 1 or n == 2500:
        extremos = True

print(f'Números divisibles por 4 y no por 8: {div_4}')
print(f'Números divisibles por 4 y 8: {div_4_8}')
if may_2000 > 0:
    print(f'Promedio de valores mayores a 2500: {round(total_may_2000 / may_2000, 2)}')
else:
    print('No se generaron valores mayores a 2000.')
print(f'Números menores al primer valor: {men_primero}; Porcentaje del total de '
      f'números que representan: {round(men_primero / 1000 * 100, 2)}%')
if extremos:
    print(f'Al menos una vez aparecieron los extremos de la secuencia [1, 2500]')
else:
    print('No aparecieron los extremos de la secuencia')
