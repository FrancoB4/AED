"""
La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).

Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:

a) Determinar y mostrar el nombre del ganador de la carrera.

b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor
al tiempo record, mostrar un mensaje.

c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.
"""

n = int(input('Ingrese el numero de competidores: '))
best_name = None
best_time = 0
suma = 0

for i in range(1, n + 1):
    name = input(f'Ingrese el nombre del competidor {i}: ')
    time = int(input('Ingrese su tiempo en segundos: '))

    if time < best_time or i == 1:
        best_name = name
        best_time = time

    suma += time

print(f'El ganador fue {best_name}, con un tiempo de {best_time} segundos.')
print(f'El tiempo promedio de los ciclistas fue de {round(suma/n, 2)}.')
record = int(input('Ingrese el record de registrado para esta carrera: '))

if record > best_time:
    print(f'{best_name} ha logrado un nuevo record para esta carrera con un tiempo de {best_time} segundos.')
elif record == best_time:
    print(f'{best_name} ha logrado igualar el record actual de menor tiempo para esta carrera.')
else:
    print(f'El record actual sigue siendo {record} segundos.')
