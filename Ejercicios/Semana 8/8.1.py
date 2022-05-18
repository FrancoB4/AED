"""
Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar

a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia

b) Determinar la cantidad de números que son el cuadrado del número anterior

c) Determinar la posición del mayor elemento impar de la secuencia
"""

div_3 = 0
cuad_anterior = 0
may_impar = 0
n = 0
pos = 0
anterior = 0

while True:
    num = int(input('Primer numero de la secuencia: '))
    if num != 0:
        break
    else:
        print('Ingrese un numero distinto de 0...')

while num != 0:
    n += 1
    if num % 3 == 0:
        div_3 += 1
    if num % 2 != 0 and num > may_impar:
        may_impar = num
        pos = n
    if anterior ** 2 == num:
        cuad_anterior += 1

    anterior = num
    num = int(input('Siguiente numero: '))

print(f'Los números divisibles por 3 representan el {round(div_3 / n * 100, 2)}% del total.')
print(f'Hay un total de {cuad_anterior} números que son el cuadrado del anterior.')
print(f'El mayor elemento impar se ubica en la posición {pos}')
