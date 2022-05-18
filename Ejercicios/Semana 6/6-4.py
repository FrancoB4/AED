import random
a = 0
suma = 0
while a < 1000:
    suma += random.randint(0, 100000)
    a += 1

print(f'Promedio: {suma/a}')
