"""
Escribir un programa que permita leer la cantidad de números enteros ingresados por el usuario y calcular lo siguiente:

a) El segundo menor

b) El promedio de los números positivos.

c) El mayor de los números negativos.
"""
men = 0
seg_men = None
pos = 0
pos_sum = 0
may_neg = 0

n = 0

while n <= 0:
    n = int(input('Ingrese n: '))

for i in range(1, n + 1):
    num = int(input(f'Ingrese el numero {i}: '))

    if num < 0:
        if num > may_neg or may_neg == 0:
            may_neg = num
    elif num > 0:
        pos_sum += num
        pos += 1

    if i == 0:
        men = num
    elif num < men:
        seg_men = men
        men = num
    elif seg_men is None or num < seg_men:
        seg_men = num

print(f'El segundo menor numero ingresado fue: {seg_men}')
print(f'El mayor de los números negativos ingresados fue: {may_neg}')
if pos != 0:
    print(f'El promedio de los números positivos ingresados fue: {round(pos_sum/pos, 2)}')
else:
    print('no se han ingresado números positivos.')
