"""
Ingresar un secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar:

a) El promedio de los números que son múltiplos de 6

b) Cantidad de números que son divisor exacto del anterior

c) Indicar la cantidad de veces que se generó una secuencia ascendente de 3 o más números impares
"""

mult_6 = 0
total_mult_6 = 0
div_anterior = 0
seq_asc_3_imp = 0
seq_asc_flag = False

cont = 0

n = 0
while n == 0:
    n = int(input('Ingrese el primer numero de la secuencia: '))
    if n == 0:
        print('Ingrese un valor mayor que cero')

while n != 0:
    if n % 6 == 0:
        mult_6 += 1
        total_mult_6 += n

    if cont != 0 and anterior % n == 0:
        div_anterior += 1

    if (cont > 1 and n % 2 != 0 and anterior % 2 != 0 and seg_anterior % 2 != 0 and
            seg_anterior < anterior < n and not seq_asc_flag):
        seq_asc_3_imp += 1
        seq_asc_flag = True
    elif cont > 1 and not(n % 2 != 0 and anterior % 2 != 0 and seg_anterior % 2 != 0 and seg_anterior < anterior < n):
        seq_asc_flag = False

    if cont >= 1:
        seg_anterior = anterior

    anterior = n
    n = int(input('Siguiente numero: '))
    cont += 1

print(f'Promedio múltiplos de 6: {round(total_mult_6 / mult_6, 2)}')
print(f'Cantidad de números que son divisores exactos del anterior: {div_anterior}')
print(f'Cantidad de secuencias ascendentes de tres o mas números impares: {seq_asc_3_imp}')
