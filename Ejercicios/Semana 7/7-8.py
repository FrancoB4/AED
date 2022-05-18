"""
Un club náutico de la costa del lago San Roque necesita calcular estadísticas acerca de los barcos que tiene en la
guardería.

Se pretende un programa que cargue uno por uno los datos de cada barco. De ellos se sabe el nombre, el tipo (1 si es
velero, 2 si es lancha) y el monto que pagan por mes de guardería.

El programa debe cargar datos de los barcos de acuerdo a una cantidad n que se carga al comienzo y una vez completada
la carga informar:

El total anual aportado por los veleros y el total anual aportado por las lanchas (2 totales).

El nombre del velero que mayor cuota mensual paga de guardería y el valor de su cuota mensual.

El valor promedio de cuota pagada por las embarcaciones de la guardería teniendo en cuenta todas las embarcaciones
independientemente del tipo que tengan.

El porcentaje que representa el monto mensual recaudado por los veleros sobre el total mensual recaudado y el
porcentaje que representa el monto mensual recaudado por las lanchas sobre el total mensual recaudado (2 porcentajes).
"""

n = int(input('Ingrese la cantidad de embarcaciones a cargar: '))
nombre_velero_mayor = None
cuota_mayor = 0
total_veleros = 0
total_lanchas = 0

for i in range(1, n + 1):
    nombre = input(f'Nombre de la embarcación {i}: ')
    tipo = int(input(f'Tipo de la embarcación {i} [1 velero | 2 lancha]: '))
    while tipo != 1 and tipo != 2:
        tipo = int(input(f'Ingrese un tipo valido de embarcación [1 velero | 2 lancha]: '))
    cuota = float(input(f'Ingrese la cuota que paga la embarcación {i}: '))

    if tipo == 1:
        total_veleros += cuota
        if cuota > cuota_mayor:
            cuota_mayor = cuota
            nombre_velero_mayor = nombre
    else:
        total_lanchas += cuota

total = total_lanchas + total_veleros
print(f'Total veleros: ${total_veleros}.')
print(f'Total lanchas: ${total_lanchas}.')
print(f'Velero mayor cuota: {nombre_velero_mayor}; Cuota mayor veleros: ${cuota_mayor}.')
print(f'Promedio de cuota pagada: {round(total / n, 2)}')
print(f'Porcentaje veleros: {round(total_veleros / total * 100, 2)}%; Porcentaje '
      f'lanchas: {round(total_lanchas / total * 100, 2)}%')
