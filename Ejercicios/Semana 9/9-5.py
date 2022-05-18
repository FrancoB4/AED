"""
Desarrolle un programa completo en Python que permita generar una sucesión de 25000 números enteros aleatorios, usando
como semilla del generador el número 20220512 (es decir random.seed(20220512)). Los valores de cada uno de esos 25000
números deben estar entre 1 y 45000 (incluidos ambos) (DEBE usar random.randint(1, 50000) para generar esos números).
A partir de esa sucesión el programa debe:

* Determinar la cantidad de números múltiplos de 3 y también la cantidad de números múltiplos de 5 pero no de 3 y
  finalmente la cantidad de números que no cumplen ninguna de las 2 condiciones.
* Indicar el mayor entre todos los números comienzan con el dígito 1, es decir 1234 comienza con 1 y 2345 no comienza
  con 1.
* Indicar el promedio entero truncado de los números generados que son pares y múltiplos de 11.
* Indicar el porcentaje entero que representa cada contador del punto 1. Aclaración 1: NO se pide el porcentaje
  redondeado, sino el porcentaje truncado, sin decimales. Aclaración 2: en el cálculo de este porcentaje, haga primero
  la multiplicación que corresponda, y luego la división.
* Cuando finalice, en las consignas que siguen en este mismo cuestionario, se le pedirá que informe cada uno de
  estos resultados, y también se le pedirá que suba el archivo de código fuente con el programa desarrollado (por lo que
  tenga muy presente en donde dejó ese archivo). Habrá también UNA pregunta de opciones múltiples referida a este mismo
  enunciado o a temas relacionados con él.
"""
import random
random.seed(20220512)
mult_3 = mult_5 = no_mult_3_5 = may_inicia_1 = par_mult_11 = total_par_mult_11 = 0

for i in range(25000):
    num = random.randint(1, 45000)

    if num % 3 == 0:
        mult_3 += 1
    elif num % 5 == 0:
        mult_5 += 1
    else:
        no_mult_3_5 += 1

    if int(str(num)[0]) == 1 and (i == 0 or num > may_inicia_1):
        may_inicia_1 = num

    if num % 2 == 0 and num % 11 == 0:
        par_mult_11 += 1
        total_par_mult_11 += num

prom_entero_par_mult_11 = total_par_mult_11 // par_mult_11
porcentaje_mult_3 = (mult_3 * 100) // 25000
porcentaje_mult_5 = (mult_5 * 100) // 25000
porcentaje_no_mult_3_5 = (no_mult_3_5 * 100) // 25000


print(f'Múltiplos de 3: {mult_3}')
print(f'Múltiplos de 5 y no de 3: {mult_5}')
print(f'Números que no son múltiplos de 3 ni de 5: {no_mult_3_5}')
print(f'Mayor de los números iniciados en 1: {may_inicia_1}')
print(f'Promedio entero truncado de números pares múltiplos de 11: {prom_entero_par_mult_11}')
print(f'Porcentaje múltiplos de 3: {porcentaje_mult_3}%; Múltiplos de 5 y no de 3: {porcentaje_mult_5}%; '
      f'Porcentaje no múltiplos de 3 ni de 5: {porcentaje_no_mult_3_5}%')
