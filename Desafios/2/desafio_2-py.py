n = 1
while n <= 1:
    n = int(input('N: '))
    if n <= 1:
        print('Ingrese un valor positivo mayor que 1.')

long_de_la_orbita = 1
suma = n
may = 0
orbita_de_n = [n]

while n != 1:

    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    if n > may:
        may = n

    long_de_la_orbita += 1
    suma += n
    orbita_de_n.append(n)

promedio = round(suma / long_de_la_orbita, 1)

print(f'Orbita: {orbita_de_n}')
print(f'Longitud de la orbita: {long_de_la_orbita}')
print(f'Promedio de los valores de la orbita: {promedio}')
print(f'Mayor: {may}')
