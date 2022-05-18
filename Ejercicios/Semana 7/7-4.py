"""
Generar n números aleatorios entre el rango de 5000 y 450000, por cada uno de ellos mostrar y generar el
número hexadecimal
"""
import random

n = int(input('n: '))

for i in range(n):
    number = random.randint(5000, 450000)
    print(f'{number}: {hex(number)}')

print('End...')

# for i in range(n):
#     numero = random.randrange(5000, 450000)
#     hexadecimal = ''
#     #proceso de conversion hexadecimal
#     valor = numero % 16
#     siguiente = numero // 16
#     digito = ''
#     while valor > 0:
#         if valor < 10:
#             digito = str(valor)
#         else:
#             digito = chr(55 + valor)
#         hexadecimal = digito + hexadecimal
#         valor = siguiente % 16
#         siguiente //= 16
#
#     print('El numero ', numero, 'en hexadecimal es', hexadecimal)
