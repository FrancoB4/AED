"""Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce:
cantidad de espectadores y descuento (S/N). La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).

El programa deberá:

a) Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $50 en los días con
descuento y $75 en los días sin descuento.

b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre el total de funciones.
"""

total_funciones = 0
cant_descuento = 0
recaudacion = 0
espectadores = int(input('Ingrese la cantidad de espectadores de la primer función: '))

while espectadores >= 0:
    descuento = input('Hubo descuento? (S/N): ')
    total_funciones += 1

    if descuento == 'S':
        recaudacion += espectadores * 50
        cant_descuento += 1
    else:
        recaudacion += espectadores * 75

    espectadores = int(input('Ingrese la cantidad de espectadores de la siguiente función: '))

print(f'La recaudación total fue: {recaudacion}')
print(f'Hubo un total de {cant_descuento} funciones con descuento, lo que representa un '
      f'{cant_descuento/total_funciones*100} del total de funciones')
