segundos_entrada = int(input('Ingrese una cantidad de segundos: '))

horas = segundos_entrada // 3600
minutos = (segundos_entrada % 3600) // 60
segundos_salida = (segundos_entrada % 3600) % 60

print(' - ', segundos_entrada, 'son: ', horas, ':', minutos, ':', segundos_salida)
print(f' - {segundos_entrada} son: {horas}:{minutos}:{segundos_salida}')

